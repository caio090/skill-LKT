#!/usr/bin/env python3
"""Registro canônico de skills do LKT System.

Gera registry/skills.json a partir da árvore real (.claude/skills e terceiros/)
combinada com a curadoria em registry/fontes.json, valida o resultado e gera o
catálogo Markdown. Sem dependências externas; compatível com Python 3.9+.

Uso:
  python3 tools/registro.py build      # (re)gera registry/skills.json
  python3 tools/registro.py check      # falha se o registro estiver desatualizado ou inválido
  python3 tools/registro.py catalogo   # (re)gera docs/catalogo-skills.md
  python3 tools/registro.py check --catalogo  # também confere o catálogo
"""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FONTES = ROOT / "registry" / "fontes.json"
SAIDA = ROOT / "registry" / "skills.json"
SCHEMA = ROOT / "registry" / "skills.schema.json"
CATALOGO = ROOT / "docs" / "catalogo-skills.md"
IGNORAR = {"node_modules", ".git", "__pycache__", ".venv"}
ESTADOS_INSTALAVEIS = {"aprovada"}


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def hash_arvore(pasta):
    """Hash estável da pasta inteira (caminho relativo + conteúdo de cada arquivo)."""
    h = hashlib.sha256()
    for f in sorted(p for p in pasta.rglob("*") if p.is_file() and not (IGNORAR & set(p.parts))):
        h.update(f.relative_to(pasta).as_posix().encode())
        h.update(b"\0")
        h.update(f.read_bytes())
        h.update(b"\0")
    return h.hexdigest()


def frontmatter(texto):
    texto = texto.lstrip("﻿")
    m = re.match(r"^---\r?\n(.*?)\r?\n---", texto, re.S)
    if not m:
        return None
    fm = m.group(1)
    campos = {}
    nome = re.search(r"^name:\s*[\"']?([^\"'\n]+?)[\"']?\s*$", fm, re.M)
    campos["name"] = nome.group(1).strip() if nome else None
    d = re.search(r"^description:\s*(.*?)(?=^\S[\w-]*:|\Z)", fm, re.M | re.S)
    if d:
        desc = re.sub(r"^[>|]-?\s*", "", d.group(1).strip())
        desc = re.sub(r"\s+", " ", desc).strip().strip("\"'")
        campos["description"] = desc
    else:
        campos["description"] = None
    return campos


def resumo(desc, limite=180):
    if not desc:
        return ""
    primeira = re.split(r"(?<=[.!?])\s", desc, maxsplit=1)[0]
    return primeira if len(primeira) <= limite else primeira[: limite - 3].rstrip() + "..."


def descobrir():
    """Lista (id, pasta, namespace) de toda skill física versionável."""
    achados = []
    base = ROOT / ".claude" / "skills"
    for pasta in sorted(p for p in base.iterdir() if p.is_dir()):
        achados.append((pasta.name, pasta, "claude"))
    plugins = ROOT / "terceiros" / "codex" / "plugins"
    if plugins.exists():
        for plugin in sorted(p for p in plugins.iterdir() if p.is_dir()):
            for skill in sorted((plugin / "skills").glob("*/SKILL.md")):
                achados.append((f"codex.{plugin.name}/{skill.parent.name}", skill.parent, f"codex-plugin:{plugin.name}"))
    avulsas = ROOT / "terceiros" / "codex" / "skills"
    if avulsas.exists():
        for skill in sorted(avulsas.glob("*/SKILL.md")):
            achados.append((f"codex/{skill.parent.name}", skill.parent, "codex-avulsa"))
    return achados


def construir():
    cur = json.loads(FONTES.read_text(encoding="utf-8"))
    fontes, cats = cur["fontes"], cur["categorias"]
    terc, apos, codex = cur["terceiros_em_claude"], cur["aposentadas"], cur["terceiros_codex"]
    cat_de = {}
    for c, nomes in cats.items():
        for n in nomes:
            cat_de[n] = c
    registros = []
    for sid, pasta, ns in descobrir():
        arq = pasta / "SKILL.md"
        fm = frontmatter(arq.read_text(encoding="utf-8")) if arq.exists() else None
        nome = pasta.name
        licencas = sorted(p.name for p in pasta.iterdir() if p.is_file() and p.name.upper().startswith("LICEN"))
        reg = {
            "id": sid,
            "nome": (fm or {}).get("name") or nome,
            "descricao": resumo((fm or {}).get("description")),
            "categoria": None,
            "caminho": pasta.relative_to(ROOT).as_posix(),
            "hash_skill_md": sha256_bytes(arq.read_bytes()) if arq.exists() else None,
            "hash_arvore": hash_arvore(pasta),
            "arquivos_licenca": licencas,
            "origem_tipo": None,
            "fonte": None,
            "repositorio": None,
            "licenca": None,
            "evidencia_licenca": None,
            "versao_origem": None,
            "estado_upstream": "nao_verificado",
            "estado": None,
            "mecanismo_instalacao": None,
            "dependencias": [],
            "ambientes": {},
            "testes": ["tools/validar.js (frontmatter)", "tools/registro.py check"],
            "revisao": cur["revisao"],
            "observacoes": None,
            "substituta": None,
            "duplicata_intencional": None,
        }
        if ns == "claude":
            reg["categoria"] = cat_de.get(nome)
            reg["mecanismo_instalacao"] = "tools/instalar_lkt.py (cópia controlada para .claude/skills ou .agents/skills)"
            reg["ambientes"] = {"claude-code": "formato_valido", "codex": "formato_valido_nao_testado", "chatgpt": "sem_instalacao_local"}
            if nome in terc:
                t = terc[nome]
                f = fontes[t["fonte"]]
                reg.update(origem_tipo="externa", fonte=t["fonte"], repositorio=f["repositorio"], licenca=f["licenca"],
                           evidencia_licenca=f["evidencia_licenca"], versao_origem=f.get("versao"),
                           estado_upstream=t.get("upstream", "nao_verificado"), dependencias=t.get("dependencias", []),
                           observacoes=t.get("observacao") or t.get("adaptacao"),
                           duplicata_intencional=t.get("duplicata_intencional"))
                ok = f["licenca"] not in (None, "nao_verificado") and licencas
                reg["estado"] = "aprovada" if ok else "pendente"
            else:
                fonte = "lkt-plus" if nome in apos else "lkt-system"
                f = fontes[fonte]
                reg.update(origem_tipo="autoral", fonte=fonte, repositorio=f["repositorio"], licenca=f["licenca"],
                           evidencia_licenca=f["evidencia_licenca"], versao_origem=f.get("versao"), estado_upstream="nao_aplicavel")
                reg["estado"] = "aposentada" if nome in apos else "aprovada"
                if nome in apos:
                    reg["substituta"] = apos[nome]["substituta"]
                    reg["observacoes"] = apos[nome]["motivo"]
        else:
            plugin = ns.split(":", 1)[1] if ":" in ns else "_skills_avulsas"
            t = codex[plugin]
            f = fontes[t["fonte"]]
            reg.update(categoria="referencia-codex", origem_tipo="externa", fonte=t["fonte"], repositorio=f["repositorio"],
                       licenca=f["licenca"], evidencia_licenca=f["evidencia_licenca"], versao_origem=f.get("versao"),
                       estado=t["estado"], mecanismo_instalacao="referência: instalar pelo marketplace oficial do Codex; não é copiada pelo instalador",
                       ambientes={"claude-code": "nao_suportado_sem_adaptacao", "codex": "plugin_oficial", "chatgpt": "sem_instalacao_local"})
            if not licencas and plugin == "_skills_avulsas":
                reg["estado"] = "pendente"
        registros.append(reg)
    return registros


def carregar_schema():
    return json.loads(SCHEMA.read_text(encoding="utf-8"))


def validar(registros):
    erros = []
    sch = carregar_schema()
    obrig = sch["items"]["required"]
    enums = {k: set(v["enum"]) for k, v in sch["items"]["properties"].items() if "enum" in v}
    ids = set()
    for r in registros:
        for k in obrig:
            if k not in r:
                erros.append(f"{r.get('id')}: campo obrigatório ausente: {k}")
        for k, valores in enums.items():
            if r.get(k) not in valores:
                erros.append(f"{r['id']}: valor inválido em {k}: {r.get(k)!r}")
        if r["id"] in ids:
            erros.append(f"ID duplicado: {r['id']}")
        ids.add(r["id"])
        if r["hash_skill_md"] is None:
            erros.append(f"{r['id']}: pasta sem SKILL.md")
        if r["caminho"].startswith(".claude/skills") and r["categoria"] is None:
            erros.append(f"{r['id']}: sem categoria em registry/fontes.json")
        if r["origem_tipo"] == "externa" and r["estado"] == "aprovada" and not r["arquivos_licenca"]:
            erros.append(f"{r['id']}: externa aprovada sem arquivo de licença na pasta")
        if r["estado"] == "aprovada" and r["licenca"] == "nao_verificado":
            erros.append(f"{r['id']}: aprovada com licença não verificada")
    # mesmo conteúdo sob dois IDs exige justificativa explícita
    por_hash = {}
    for r in registros:
        por_hash.setdefault(r["hash_arvore"], []).append(r)
    for grupo in por_hash.values():
        if len(grupo) > 1:
            justificados = {r["duplicata_intencional"] for r in grupo if r["duplicata_intencional"]}
            outros = {r["id"] for r in grupo}
            if not (justificados & outros):
                erros.append("Conteúdo idêntico sem justificativa: " + ", ".join(sorted(outros)))
    cur = json.loads(FONTES.read_text(encoding="utf-8"))
    fisicos = {r["id"] for r in registros}
    for nome in list(cur["terceiros_em_claude"]) + list(cur["aposentadas"]):
        if nome not in fisicos:
            erros.append(f"registry/fontes.json cita {nome}, que não existe em .claude/skills")
    return erros


def serializar(registros):
    return json.dumps({"_gerado_por": "tools/registro.py build — não editar à mão", "total": len(registros), "skills": registros},
                      ensure_ascii=False, indent=1) + "\n"


ROTULO = {"aprovada": "aprovada", "pendente": "pendente", "bloqueada": "bloqueada", "referencia": "referência", "aposentada": "aposentada", "candidata": "candidata"}


def gerar_catalogo(registros):
    claude = [r for r in registros if r["caminho"].startswith(".claude/skills")]
    codex = [r for r in registros if not r["caminho"].startswith(".claude/skills")]
    cont = {}
    for r in claude:
        cont[(r["origem_tipo"], r["fonte"], r["estado"])] = cont.get((r["origem_tipo"], r["fonte"], r["estado"]), 0) + 1
    nucleo = sum(1 for r in claude if r["fonte"] == "lkt-system")
    plus = sum(1 for r in claude if r["fonte"] == "lkt-plus")
    ext = sum(1 for r in claude if r["origem_tipo"] == "externa")
    linhas = [
        "# Catálogo de skills",
        "",
        "> Arquivo GERADO por `python3 tools/registro.py catalogo` a partir de",
        "> [`registry/skills.json`](../registry/skills.json). Não editar à mão: altere",
        "> [`registry/fontes.json`](../registry/fontes.json) ou a skill e gere de novo.",
        "",
        f"Em `.claude/skills/`: **{len(claude)}** skills — {nucleo} do núcleo LKT System, {plus} do LKT Plus "
        f"(aposentadas, mantidas só como histórico) e {ext} de terceiros.",
        f"Em `terceiros/codex/`: **{len(codex)}** skills de referência para o Codex (não instaladas pelo instalador).",
        "",
        "Estados: **aprovada** (pode ser instalada) · **pendente** (falta verificar origem/licença) ·",
        "**bloqueada** (licença impede redistribuição) · **referência** (instalar pela fonte oficial) ·",
        "**aposentada** (substituída; não instalar).",
        "",
        "Origem e licença detalhadas: [`skills-terceiros.md`](skills-terceiros.md) e [`licencas.md`](licencas.md).",
        "",
    ]
    por_cat = {}
    for r in claude:
        por_cat.setdefault(r["categoria"] or "sem-categoria", []).append(r)
    for cat in sorted(por_cat):
        linhas += [f"## {cat}", "", "| Skill | Descrição | Origem | Estado |", "|---|---|---|---|"]
        for r in sorted(por_cat[cat], key=lambda x: x["id"]):
            origem = "LKT System" if r["fonte"] == "lkt-system" else ("LKT Plus" if r["fonte"] == "lkt-plus" else f"{r['fonte']} · {r['licenca']}")
            desc = (r["descricao"] or "").replace("|", "\\|")
            estado = ROTULO.get(r["estado"], r["estado"])
            if r["substituta"]:
                estado += f" → `{r['substituta']}`"
            linhas.append(f"| `{r['id']}` | {desc} | {origem} | {estado} |")
        linhas.append("")
    linhas += ["## Referência Codex (`terceiros/codex/`)", "", "| ID | Fonte | Licença | Estado |", "|---|---|---|---|"]
    for r in sorted(codex, key=lambda x: x["id"]):
        linhas.append(f"| `{r['id']}` | {r['fonte']} | {r['licenca']} | {ROTULO.get(r['estado'], r['estado'])} |")
    linhas += [
        "",
        "## Skills obrigatórias em cadeia",
        "",
        "Para páginas, sites, landing pages, dashboards, portais ou interfaces:",
        "",
        "1. `pagina-e-site`",
        "2. `design-front-end`",
        "3. `texto-natural-pt-br`",
        "",
        "Para qualquer texto voltado ao público final, aplicar `texto-natural-pt-br`",
        "ao final do fluxo, independente da skill principal usada. Regras de",
        "precedência completas em [`roteamento.md`](roteamento.md).",
        "",
    ]
    return "\n".join(linhas)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("acao", choices=["build", "check", "catalogo"])
    ap.add_argument("--catalogo", action="store_true", help="em check, também confere docs/catalogo-skills.md")
    a = ap.parse_args(argv)
    registros = construir()
    erros = validar(registros)
    if a.acao == "build":
        SAIDA.write_text(serializar(registros), encoding="utf-8")
        print(f"registry/skills.json: {len(registros)} skills")
    elif a.acao == "catalogo":
        CATALOGO.write_text(gerar_catalogo(registros), encoding="utf-8")
        print("docs/catalogo-skills.md gerado")
    else:
        if not SAIDA.exists() or SAIDA.read_text(encoding="utf-8") != serializar(registros):
            erros.append("registry/skills.json desatualizado: rode `python3 tools/registro.py build`")
        if a.catalogo and (not CATALOGO.exists() or CATALOGO.read_text(encoding="utf-8") != gerar_catalogo(registros)):
            erros.append("docs/catalogo-skills.md desatualizado: rode `python3 tools/registro.py catalogo`")
    estados = {}
    for r in registros:
        estados[r["estado"]] = estados.get(r["estado"], 0) + 1
    print("Estados:", ", ".join(f"{k}={v}" for k, v in sorted(estados.items(), key=lambda x: str(x[0]))))
    if erros:
        print(f"ERROS ({len(erros)}):")
        for e in erros:
            print("  -", e)
        return 1
    print("OK: registro válido")
    return 0


if __name__ == "__main__":
    sys.exit(main())
