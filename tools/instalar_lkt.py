#!/usr/bin/env python3
"""Instalador LKT: copia skills originais para outro projeto."""
import argparse
import shutil
from pathlib import Path

PERFIS = {
    "base": ["texto-natural-pt-br", "humanizer-pt-br", "qa"],
    "web": ["pagina-e-site", "design-front-end", "app-e-sistema", "seo"],
    "marketing": ["estrategia-de-marketing", "calendario-de-conteudo", "anuncio-meta"],
    "automacao": ["automacao-fluxos", "integrar-api", "planejar-banco-de-dados"],
}
def main():
    p = argparse.ArgumentParser()
    p.add_argument("--project", type=Path, required=True)
    p.add_argument("--profile", choices=["auto", *PERFIS], default="auto")
    p.add_argument("--include", action="append", default=[])
    p.add_argument("--apply", action="store_true")
    args = p.parse_args()
    root = Path(__file__).resolve().parents[1]
    target = args.project.resolve()
    if not target.is_dir() or target == root or root in target.parents:
        p.error("Informe um projeto existente fora da biblioteca LKT")
    sources = [
        root / ".claude/skills",
        root / "vendor/tayannara-skills/.claude/skills",
        root / "vendor/superpowers/skills",
    ]
    available = {}
    for folder in sources:
        if folder.exists():
            for file in sorted(folder.rglob("SKILL.md")):
                available.setdefault(file.parent.name, file.parent)
    profile = args.profile
    if profile == "auto":
        profile = "web" if (target / "package.json").exists() else "base"
    names = list(dict.fromkeys(PERFIS["base"] + PERFIS.get(profile, []) + args.include))
    for name in names:
        source = available.get(name)
        destination = target / ".claude/skills" / name
        if source is None:
            print(f"AUSENTE: {name} (verifique os submodulos e permissoes)")
        elif destination.exists():
            print(f"EXISTENTE: {name}, preservado")
        elif args.apply:
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(source, destination)
            print(f"INSTALADO: {name}")
        else:
            print(f"PREVISTO: {name} <- {source}")
    print("Modo:", "aplicado" if args.apply else "simulacao")
if __name__ == "__main__":
    main()
