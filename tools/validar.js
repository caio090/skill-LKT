#!/usr/bin/env node
// Validador estrutural do REC OS — sem dependências externas.
// Uso: node tools/validar.js

const fs = require("fs");
const path = require("path");

const ROOT = path.resolve(__dirname, "..");
const KEBAB = /^[a-z0-9]+(-[a-z0-9]+)*$/;
const problems = [];
const warnings = [];
const info = [];

function listDirs(dir) {
  if (!fs.existsSync(dir)) return [];
  return fs
    .readdirSync(dir, { withFileTypes: true })
    .filter((d) => d.isDirectory())
    .map((d) => d.name);
}

function listFiles(dir, ext) {
  if (!fs.existsSync(dir)) return [];
  return fs
    .readdirSync(dir, { withFileTypes: true })
    .filter((d) => d.isFile() && (!ext || d.name.endsWith(ext)))
    .map((d) => d.name);
}

function walkMarkdown(dir, acc = []) {
  if (!fs.existsSync(dir)) return acc;
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      if (entry.name === "node_modules") continue;
      walkMarkdown(full, acc);
    } else if (entry.isFile() && entry.name.endsWith(".md")) {
      acc.push(full);
    }
  }
  return acc;
}

// 1. Nomenclatura de pastas (kebab-case) em modules/, templates/, .claude/skills/
for (const base of ["modules", "templates", path.join(".claude", "skills")]) {
  for (const name of listDirs(path.join(ROOT, base))) {
    if (!KEBAB.test(name)) {
      problems.push(`Nomenclatura fora do padrão (kebab-case): ${base}/${name}`);
    }
  }
}

// 2. Skills: cada pasta deve ter SKILL.md com name/description no frontmatter
const skillsDir = path.join(ROOT, ".claude", "skills");
const skillNames = new Set();
const skillDirs = listDirs(skillsDir);
for (const name of skillDirs) {
  const skillFile = path.join(skillsDir, name, "SKILL.md");
  if (!fs.existsSync(skillFile)) {
    problems.push(`Skill sem SKILL.md: .claude/skills/${name}/`);
    continue;
  }
  const content = fs.readFileSync(skillFile, "utf8").replace(/^﻿/, "");
  const match = content.match(/^---\r?\n([\s\S]*?)\r?\n---/);
  if (!match) {
    problems.push(`SKILL.md sem frontmatter YAML: .claude/skills/${name}/SKILL.md`);
    continue;
  }
  const frontmatter = match[1];
  const hasName = /^name:\s*\S+/m.test(frontmatter);
  const hasDesc = /^description:\s*\S+/m.test(frontmatter);
  if (!hasName) problems.push(`SKILL.md sem campo "name": .claude/skills/${name}/SKILL.md`);
  if (!hasDesc) problems.push(`SKILL.md sem campo "description": .claude/skills/${name}/SKILL.md`);
  const nameMatch = frontmatter.match(/^name:\s*(\S+)/m);
  if (nameMatch) {
    const declared = nameMatch[1];
    if (declared !== name) {
      warnings.push(`Nome declarado difere da pasta: .claude/skills/${name}/SKILL.md tem name: ${declared}`);
    }
    if (skillNames.has(declared)) {
      problems.push(`Skill duplicada: name "${declared}" aparece mais de uma vez`);
    }
    skillNames.add(declared);
  }
}
// Arquivos soltos em .claude/skills/ (fora de pasta) — erro comum de estrutura
for (const file of listFiles(skillsDir)) {
  problems.push(`Arquivo solto em .claude/skills/ (deveria estar em uma subpasta com SKILL.md): ${file}`);
}

// 3. Referências remanescentes a MazyOS / LKT Plus dentro do próprio REC OS
const allMd = walkMarkdown(ROOT);
const refPattern = /MazyOS|LKT[\s-]?Plus|lkt-plus/gi;
const EXPECTED_REFS = new Set([
  "CLAUDE.md",
  "AGENTS.md",
  "README.md",
  path.join("docs", "manifesto.md"),
  path.join("docs", "roteamento.md"),
  path.join("_memoria", "pendencias.md"),
  "CHANGELOG.md",
  path.join("docs", "catalogo-skills.md"),
  path.join("docs", "skills-terceiros.md"),
  path.join("docs", "MIGRACAO.md"),
  path.join("docs", "licencas.md"),
  // skills que documentam a migração ou foram aposentadas (histórico)
  path.join(".claude", "skills", "instalar", "SKILL.md"),
  path.join(".claude", "skills", "validar-sistema", "SKILL.md"),
  path.join(".claude", "skills", "salvar", "SKILL.md"),
  path.join(".claude", "skills", "atualizar", "SKILL.md"),
]);
for (const file of allMd) {
  const rel = path.relative(ROOT, file);
  if (EXPECTED_REFS.has(rel) || rel.startsWith(path.join("docs", "auditorias") + path.sep)) {
    continue; // referências esperadas (documentação da migração)
  }
  const content = fs.readFileSync(file, "utf8");
  if (refPattern.test(content)) {
    warnings.push(`Referência a MazyOS/LKT Plus encontrada em: ${rel}`);
  }
}

// 4. Links relativos quebrados em Markdown
// Conteúdo de terceiros (terceiros/, vendor/ e skills externas do registro) não é
// editado pelo LKT: link quebrado ali vira aviso, não erro.
const { extrairLinks } = require("./lib/links.js");
const externas = new Set();
const registroPath = path.join(ROOT, "registry", "skills.json");
if (fs.existsSync(registroPath)) {
  for (const r of JSON.parse(fs.readFileSync(registroPath, "utf8")).skills) {
    if (r.origem_tipo === "externa") externas.add(r.caminho + "/");
  }
}
function ehTerceiro(rel) {
  const posix = rel.split(path.sep).join("/");
  if (posix.startsWith("terceiros/") || posix.startsWith("vendor/")) return true;
  for (const prefixo of externas) if (posix.startsWith(prefixo)) return true;
  return false;
}
let linksTerceiros = 0;
for (const file of allMd) {
  const rel = path.relative(ROOT, file);
  const content = fs.readFileSync(file, "utf8");
  for (const target of extrairLinks(content)) {
    const resolved = path.resolve(path.dirname(file), target);
    if (!fs.existsSync(resolved)) {
      if (ehTerceiro(rel)) {
        linksTerceiros++;
        warnings.push(`Link quebrado em conteúdo de terceiros (não editado) ${rel}: ${target}`);
      } else {
        problems.push(`Link quebrado em ${rel}: ${target}`);
      }
    }
  }
}

// 4b. Registro canônico em dia (registry/skills.json e catálogo gerado)
const { spawnSync } = require("child_process");
const reg = spawnSync("python3", [path.join(ROOT, "tools", "registro.py"), "check", "--catalogo"], { encoding: "utf8" });
if (reg.error) {
  warnings.push("python3 indisponível: verificação do registro não executada");
} else if (reg.status !== 0) {
  problems.push("Registro/catálogo inválido ou desatualizado:\n" + (reg.stdout || "") + (reg.stderr || ""));
}

// 5. Catálogo de skills vs skills reais
const catalogoPath = path.join(ROOT, "docs", "catalogo-skills.md");
if (fs.existsSync(catalogoPath)) {
  const catalogo = fs.readFileSync(catalogoPath, "utf8");
  for (const name of skillDirs) {
    if (!catalogo.includes(name)) {
      warnings.push(`Skill "${name}" não aparece em docs/catalogo-skills.md`);
    }
  }
}

// Relatório
info.push(`Pastas em modules/: ${listDirs(path.join(ROOT, "modules")).length}`);
info.push(`Pastas em templates/: ${listDirs(path.join(ROOT, "templates")).length}`);
info.push(`Skills válidas: ${skillDirs.length - problems.filter((p) => p.includes("Skill sem SKILL.md")).length}`);
info.push(`Arquivos Markdown lidos: ${allMd.length}`);

console.log("=== LKT System — validação estrutural ===\n");
console.log("Resumo:");
for (const line of info) console.log(`  - ${line}`);

console.log(`\nProblemas (${problems.length}):`);
if (problems.length === 0) console.log("  - Nenhum.");
for (const p of problems) console.log(`  - ${p}`);

console.log(`\nAvisos (${warnings.length}):`);
if (warnings.length === 0) console.log("  - Nenhum.");
for (const w of warnings) console.log(`  - ${w}`);

process.exitCode = problems.length > 0 ? 1 : 0;
