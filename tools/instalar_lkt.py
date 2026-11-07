#!/usr/bin/env python3
"""Instalador LKT: instala skills aprovadas do registro em um projeto consumidor.

Simulação por padrão. Nada é escrito sem --apply.

Exemplos:
  python3 tools/instalar_lkt.py --list
  python3 tools/instalar_lkt.py --project ../meu-site --profile web            # simula
  python3 tools/instalar_lkt.py --project ../meu-site --profile web --apply    # instala
  python3 tools/instalar_lkt.py --project ../meu-site --check                  # divergências, sem escrita
  python3 tools/instalar_lkt.py --project ../meu-site --update --apply         # atualiza só o que não foi editado
  python3 tools/instalar_lkt.py --project ../meu-site --uninstall seo --apply  # remove só arquivos gerenciados
  python3 tools/instalar_lkt.py --project ../meu-site --rollback --apply       # desfaz a última operação aplicada

Runtimes: claude (.claude/skills, padrão) e codex (.agents/skills).
Manifesto do consumidor: <projeto>/.lkt/instalacao.json (hashes de cada arquivo instalado).
"""
import argparse
import datetime as dt
import hashlib
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRO = ROOT / "registry" / "skills.json"
PERFIS = ROOT / "registry" / "perfis.json"
DESTINOS = {"claude": Path(".claude/skills"), "codex": Path(".agents/skills")}
NOME_VALIDO = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
MANIFESTO = Path(".lkt/instalacao.json")


class ErroInstalacao(Exception):
    pass


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def arquivos_de(pasta):
    """Mapa relpath -> sha256. Recusa links simbólicos (origem ou destino)."""
    mapa = {}
    for p in sorted(pasta.rglob("*")):
        if p.is_symlink():
            raise ErroInstalacao(f"link simbólico recusado: {p}")
        if p.is_file():
            mapa[p.relative_to(pasta).as_posix()] = sha(p)
    return mapa


def carregar_json(path, padrao):
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else padrao


def carregar_catalogo():
    if not REGISTRO.exists():
        raise ErroInstalacao("registry/skills.json ausente: rode `python3 tools/registro.py build` na biblioteca")
    regs = json.loads(REGISTRO.read_text(encoding="utf-8"))["skills"]
    return {r["id"]: r for r in regs if r["caminho"].startswith(".claude/skills/")}


def perfis():
    return json.loads(PERFIS.read_text(encoding="utf-8"))["perfis"]


def validar_projeto(target):
    if not target.exists() or not target.is_dir():
        raise ErroInstalacao(f"projeto inexistente: {target}")
    raiz = ROOT.resolve()
    target = target.resolve()
    if target == raiz or raiz in target.parents or target in raiz.parents:
        raise ErroInstalacao("informe um projeto existente fora da biblioteca LKT (nem dentro, nem acima dela)")


def destino_seguro(target, runtime, nome):
    if not NOME_VALIDO.match(nome):
        raise ErroInstalacao(f"nome de skill inválido: {nome!r}")
    base = target / DESTINOS[runtime]
    atual = target
    for parte in DESTINOS[runtime].parts:
        atual = atual / parte
        if atual.is_symlink():
            raise ErroInstalacao(f"diretório de destino é link simbólico: {atual}")
    dest = (base / nome)
    if dest.is_symlink():
        raise ErroInstalacao(f"destino é link simbólico: {dest}")
    if target.resolve() not in dest.resolve().parents:
        raise ErroInstalacao(f"destino fora do projeto: {dest}")
    return dest


def resolver_nomes(args, cat):
    todos = perfis()
    perfil = args.profile
    if perfil == "auto":
        perfil = "web" if (args.project / "package.json").exists() else "base"
    if perfil not in todos:
        raise ErroInstalacao(f"perfil inexistente: {perfil}. Use --list")
    nomes = list(todos["base"]["skills"])
    if perfil != "base":
        nomes += todos[perfil]["skills"]
    nomes += args.include
    excl = set(args.exclude)
    return perfil, [n for n in dict.fromkeys(nomes) if n not in excl]


def planejar(args, cat, man):
    """Classifica cada skill sem escrever nada."""
    instaladas = man.get("skills", {})
    if args.update or args.check:
        nomes = sorted(instaladas)
        perfil = man.get("perfil")
    else:
        perfil, nomes = resolver_nomes(args, cat)
    plano = []
    for nome in nomes:
        if not NOME_VALIDO.match(nome):
            raise ErroInstalacao(f"nome de skill inválido: {nome!r}")
        item = {"skill": nome}
        reg = cat.get(nome)
        if reg is None:
            item["status"] = "AUSENTE"
            item["motivo"] = "não existe em .claude/skills do registro (pode ser referência externa ou nome errado)"
            plano.append(item)
            continue
        if reg["estado"] != "aprovada":
            item["status"] = "BLOQUEADA"
            item["motivo"] = f"estado '{reg['estado']}' no registro" + (f"; use {reg['substituta']}" if reg.get("substituta") else "")
            plano.append(item)
            continue
        origem = ROOT / reg["caminho"]
        if not origem.exists():
            item["status"] = "AUSENTE"
            item["motivo"] = "pasta de origem não encontrada (submódulo ou checkout incompleto?)"
            plano.append(item)
            continue
        dest = destino_seguro(args.project, args.runtime, nome)
        arq_origem = arquivos_de(origem)
        item.update(origem=reg["caminho"], destino=dest.relative_to(args.project).as_posix(), hash_origem=reg["hash_arvore"])
        gerida = instaladas.get(nome)
        if not dest.exists():
            item["status"] = "NOVA" if gerida is None else "REMOVIDA_LOCALMENTE"
            if gerida is not None:
                item["motivo"] = "consta no manifesto mas a pasta foi apagada; reinstale com --include"
        elif gerida is None:
            item["status"] = "EXISTENTE_NAO_GERENCIADA"
            item["motivo"] = "pasta já existe e não foi instalada pelo LKT: preservada"
        else:
            local = arquivos_de(dest)
            if local != gerida["arquivos"]:
                item["status"] = "CONFLITO"
                alterados = sorted(set(local.items()) ^ set(gerida["arquivos"].items()))
                item["motivo"] = "edição local detectada: " + ", ".join(sorted({a for a, _ in alterados}))
            elif arq_origem == gerida["arquivos"]:
                item["status"] = "ATUALIZADA"
            else:
                item["status"] = "ATUALIZAVEL"
        item["_arquivos_origem"] = arq_origem
        plano.append(item)
    return perfil, plano


def agora():
    return dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")


def salvar_manifesto(target, man):
    path = target / MANIFESTO
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(man, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    tmp.replace(path)


def aplicar(args, man, plano, perfil):
    """Aplica NOVA (e ATUALIZAVEL com --update). Backup antes; restaura se falhar no meio."""
    target = args.project
    acao = "atualizar" if args.update else "instalar"
    alvo = {"NOVA"} | ({"ATUALIZAVEL"} if args.update else set())
    itens = [i for i in plano if i["status"] in alvo]
    if not itens:
        return []
    carimbo = agora()
    backup = target / ".lkt" / "backup" / carimbo
    backup.mkdir(parents=True, exist_ok=True)
    (backup / "instalacao.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
    feitos, tocados = [], []
    try:
        for item in itens:
            nome = item["skill"]
            dest = target / item["destino"]
            tocados.append(nome)
            if dest.exists():
                shutil.move(str(dest), str(backup / nome))
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(str(ROOT / item["origem"]), str(dest))
            if arquivos_de(dest) != item["_arquivos_origem"]:
                raise ErroInstalacao(f"cópia de {nome} não confere com a origem")
            man.setdefault("skills", {})[nome] = {
                "origem": item["origem"], "hash_origem": item["hash_origem"],
                "arquivos": item["_arquivos_origem"], "aplicado_em": carimbo,
            }
            feitos.append(nome)
            item["status"] = "INSTALADA" if item["status"] == "NOVA" else "ATUALIZADA_AGORA"
    except Exception:
        for nome in tocados:
            shutil.rmtree(str(target / DESTINOS[args.runtime] / nome), ignore_errors=True)
            if (backup / nome).exists():
                shutil.move(str(backup / nome), str(target / DESTINOS[args.runtime] / nome))
        raise
    man.update(versao_registro=1, runtime=args.runtime, perfil=perfil or man.get("perfil"))
    man.setdefault("historico", []).append({"carimbo": carimbo, "acao": acao, "skills": feitos})
    salvar_manifesto(target, man)
    return feitos


def desinstalar(args, man):
    resultado = []
    for nome in args.uninstall:
        g = man.get("skills", {}).get(nome)
        dest = destino_seguro(args.project, args.runtime, nome)
        if g is None:
            resultado.append({"skill": nome, "status": "NAO_GERENCIADA", "motivo": "não foi instalada pelo LKT: nada removido"})
            continue
        local = arquivos_de(dest) if dest.exists() else {}
        editados = [a for a, h in g["arquivos"].items() if local.get(a) not in (None, h)]
        if editados:
            resultado.append({"skill": nome, "status": "CONFLITO", "motivo": "arquivos editados localmente: " + ", ".join(editados)})
            continue
        if args.apply:
            for rel in g["arquivos"]:
                f = dest / rel
                if f.exists():
                    f.unlink()
            for d in sorted((p for p in dest.rglob("*") if p.is_dir()), key=lambda p: -len(p.parts)) + [dest]:
                if d.exists() and not any(d.iterdir()):
                    d.rmdir()
            del man["skills"][nome]
            extras = dest.exists()
            resultado.append({"skill": nome, "status": "REMOVIDA", "motivo": "arquivos não gerenciados preservados" if extras else None})
        else:
            resultado.append({"skill": nome, "status": "REMOCAO_PREVISTA"})
    if args.apply and any(r["status"] == "REMOVIDA" for r in resultado):
        man.setdefault("historico", []).append({"carimbo": agora(), "acao": "desinstalar", "skills": [r["skill"] for r in resultado if r["status"] == "REMOVIDA"]})
        salvar_manifesto(args.project, man)
    return resultado


def reverter(args, man):
    pasta = args.project / ".lkt" / "backup"
    if not pasta.exists() or not any(pasta.iterdir()):
        raise ErroInstalacao("nenhum backup para reverter")
    ultimo = sorted(p for p in pasta.iterdir() if p.is_dir())[-1]
    anterior = json.loads((ultimo / "instalacao.json").read_text(encoding="utf-8"))
    hist = man.get("historico", [])
    feitos = hist[-1]["skills"] if hist and hist[-1]["carimbo"] == ultimo.name else []
    plano = []
    for nome in feitos:
        g = man["skills"].get(nome, {})
        dest = destino_seguro(args.project, args.runtime, nome)
        if dest.exists() and arquivos_de(dest) != g.get("arquivos"):
            raise ErroInstalacao(f"{nome} foi editada depois da operação; reversão cancelada sem alterar nada")
        plano.append((nome, dest))
    if not args.apply:
        return [{"skill": n, "status": "REVERSAO_PREVISTA", "backup": ultimo.name} for n, _ in plano]
    for nome, dest in plano:
        if dest.exists():
            shutil.rmtree(str(dest))
        if (ultimo / nome).exists():
            shutil.move(str(ultimo / nome), str(dest))
    salvar_manifesto(args.project, anterior)
    shutil.rmtree(str(ultimo))
    return [{"skill": n, "status": "REVERTIDA", "backup": ultimo.name} for n, _ in plano]


def listar(cat):
    linhas = ["Perfis:"]
    for nome, p in perfis().items():
        linhas.append(f"  {nome:14} {p['descricao']} ({len(p['skills'])} skills + base)")
    aprovadas = sorted(n for n, r in cat.items() if r["estado"] == "aprovada")
    linhas.append(f"\nSkills aprovadas para instalação ({len(aprovadas)}):")
    linhas.append("  " + " ".join(aprovadas))
    outras = sorted(f"{n}({r['estado']})" for n, r in cat.items() if r["estado"] != "aprovada")
    if outras:
        linhas.append("\nNão instaláveis: " + " ".join(outras))
    return "\n".join(linhas)


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--project", type=Path)
    p.add_argument("--profile", default="auto", help="auto, ou um perfil de registry/perfis.json")
    p.add_argument("--include", action="append", default=[])
    p.add_argument("--exclude", action="append", default=[])
    p.add_argument("--runtime", choices=sorted(DESTINOS), default="claude")
    p.add_argument("--apply", action="store_true", help="sem esta opção nada é escrito")
    p.add_argument("--list", action="store_true", help="lista perfis e skills instaláveis")
    p.add_argument("--check", action="store_true", help="compara instalação com a biblioteca, sem escrita")
    p.add_argument("--update", action="store_true", help="atualiza skills gerenciadas não editadas localmente")
    p.add_argument("--uninstall", nargs="+", default=[], metavar="SKILL")
    p.add_argument("--rollback", action="store_true", help="desfaz a última operação aplicada")
    p.add_argument("--json", action="store_true", help="saída em JSON")
    args = p.parse_args(argv)
    try:
        cat = carregar_catalogo()
        if args.list:
            print(listar(cat))
            return 0
        if args.project is None:
            p.error("--project é obrigatório (ou use --list)")
        args.project = args.project.resolve()
        validar_projeto(args.project)
        man = carregar_json(args.project / MANIFESTO, {})
        if man.get("runtime") and man["runtime"] != args.runtime and (args.update or args.check or args.rollback or args.uninstall):
            raise ErroInstalacao(f"manifesto do projeto usa runtime {man['runtime']}; passe --runtime {man['runtime']}")
        if args.rollback:
            res, perfil = reverter(args, man), man.get("perfil")
        elif args.uninstall:
            res, perfil = desinstalar(args, man), man.get("perfil")
        else:
            perfil, res = planejar(args, cat, man)
            if args.apply and not args.check:
                aplicar(args, man, res, perfil)
    except ErroInstalacao as e:
        if args.json:
            print(json.dumps({"erro": str(e)}, ensure_ascii=False))
        else:
            print(f"ERRO: {e}", file=sys.stderr)
        return 2
    for item in res:
        item.pop("_arquivos_origem", None)
    modo = "aplicado" if args.apply and not args.check else "simulacao"
    if args.json:
        print(json.dumps({"modo": modo, "runtime": args.runtime, "perfil": perfil, "itens": res}, ensure_ascii=False, indent=1))
    else:
        for item in res:
            extra = f" <- {item['origem']}" if item.get("origem") and item["status"] == "NOVA" else ""
            motivo = f" ({item['motivo']})" if item.get("motivo") else ""
            print(f"{item['status']}: {item['skill']}{extra}{motivo}")
        print(f"Modo: {modo} | runtime: {args.runtime} | perfil: {perfil}")
    return 1 if any(i["status"] == "CONFLITO" for i in res) else 0


if __name__ == "__main__":
    sys.exit(main())
