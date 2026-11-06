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
]);
for (const file of allMd) {
  const rel = path.relative(ROOT, file);
  if (EXPECTED_REFS.has(rel)) {
    continue; // referências esperadas (documentação da migração)
  }
  const content = fs.readFileSync(file, "utf8");
  if (refPattern.test(content)) {
    warnings.push(`Referência a MazyOS/LKT Plus encontrada em: ${rel}`);
  }
}

// 4. Links relativos quebrados em Markdown
const linkPattern = /\]\(([^)]+)\)/g;
for (const file of allMd) {
  const rel = path.relative(ROOT, file);
  const content = fs.readFileSync(file, "utf8");
  let m;
  while ((m = linkPattern.exec(content))) {
    const target = m[1].split("#")[0].trim();
    if (!target || /^https?:\/\//.test(target) || /^mailto:/.test(target)) continue;
    const resolved = path.resolve(path.dirname(file), target);
    if (!fs.existsSync(resolved)) {
      problems.push(`Link quebrado em ${rel}: ${target}`);
    }
  }
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

console.log("=== REC OS — validação estrutural ===\n");
console.log("Resumo:");
for (const line of info) console.log(`  - ${line}`);

console.log(`\nProblemas (${problems.length}):`);
if (problems.length === 0) console.log("  - Nenhum.");
for (const p of problems) console.log(`  - ${p}`);

console.log(`\nAvisos (${warnings.length}):`);
if (warnings.length === 0) console.log("  - Nenhum.");
for (const w of warnings) console.log(`  - ${w}`);

process.exitCode = problems.length > 0 ? 1 : 0;
