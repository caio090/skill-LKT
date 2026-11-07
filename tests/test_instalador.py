"""Testes do instalador em bibliotecas e projetos descartáveis. Sem rede.

Rodar: python3 -m unittest discover -s tests -v
"""
import contextlib
import io
import json
import os
import socket
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import instalar_lkt as inst  # noqa: E402


def sem_rede(*a, **k):
    raise AssertionError("teste tentou acessar a rede")


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        t = Path(self.tmp.name)
        self.lib = t / "biblioteca"
        self.proj = t / "projeto"
        self.proj.mkdir()
        self.skills = {}
        self.criar_skill("texto-natural-pt-br", "v1")
        self.criar_skill("qa", "v1")
        self.criar_skill("seo", "v1")
        self.criar_skill("salvar", "v1", estado="aposentada", substituta="salvar-local")
        self.criar_skill("remotion-x", "v1", estado="bloqueada")
        self.perfis = {"base": {"descricao": "b", "skills": ["texto-natural-pt-br", "qa"]},
                       "web": {"descricao": "w", "skills": ["seo"]}}
        self.gravar()
        self.patches = [mock.patch.object(inst, "ROOT", self.lib),
                        mock.patch.object(inst, "REGISTRO", self.lib / "registry/skills.json"),
                        mock.patch.object(inst, "PERFIS", self.lib / "registry/perfis.json"),
                        mock.patch.object(socket, "socket", side_effect=sem_rede)]
        for p in self.patches:
            p.start()

    def tearDown(self):
        for p in self.patches:
            p.stop()
        self.tmp.cleanup()

    def criar_skill(self, nome, versao, estado="aprovada", substituta=None):
        pasta = self.lib / ".claude/skills" / nome
        pasta.mkdir(parents=True, exist_ok=True)
        (pasta / "SKILL.md").write_text(f"---\nname: {nome}\ndescription: teste {versao}\n---\n", encoding="utf-8")
        (pasta / "ref").mkdir(exist_ok=True)
        (pasta / "ref" / "notas.md").write_text(versao, encoding="utf-8")
        self.skills[nome] = {"id": nome, "caminho": f".claude/skills/{nome}", "estado": estado,
                             "hash_arvore": versao, "substituta": substituta}

    def gravar(self):
        (self.lib / "registry").mkdir(parents=True, exist_ok=True)
        (self.lib / "registry/skills.json").write_text(json.dumps({"skills": list(self.skills.values())}), encoding="utf-8")
        (self.lib / "registry/perfis.json").write_text(json.dumps({"perfis": self.perfis}), encoding="utf-8")

    def rodar(self, *args):
        saida = io.StringIO()
        with contextlib.redirect_stdout(saida), contextlib.redirect_stderr(io.StringIO()):
            code = inst.main(["--project", str(self.proj), "--json", *args])
        return code, json.loads(saida.getvalue())

    def status(self, res):
        return {i["skill"]: i["status"] for i in res["itens"]}

    def arvore(self):
        return sorted(p.relative_to(self.proj).as_posix() for p in self.proj.rglob("*"))


class TestInstalador(Base):
    def test_simulacao_padrao_nao_escreve(self):
        code, res = self.rodar("--profile", "web")
        self.assertEqual(code, 0)
        self.assertEqual(res["modo"], "simulacao")
        self.assertEqual(self.status(res), {"texto-natural-pt-br": "NOVA", "qa": "NOVA", "seo": "NOVA"})
        self.assertEqual(self.arvore(), [])

    def test_apply_instala_e_registra_hashes(self):
        code, res = self.rodar("--profile", "base", "--apply")
        self.assertEqual(code, 0)
        self.assertTrue((self.proj / ".claude/skills/qa/ref/notas.md").exists())
        man = json.loads((self.proj / ".lkt/instalacao.json").read_text())
        self.assertIn("SKILL.md", man["skills"]["qa"]["arquivos"])
        self.assertEqual(man["runtime"], "claude")

    def test_idempotente(self):
        self.rodar("--profile", "base", "--apply")
        antes = {p: p.stat().st_mtime_ns for p in self.proj.rglob("*") if p.is_file() and "backup" not in p.parts}
        code, res = self.rodar("--profile", "base", "--apply")
        self.assertEqual(set(self.status(res).values()), {"ATUALIZADA"})
        depois = {p: p.stat().st_mtime_ns for p in self.proj.rglob("*") if p.is_file() and "backup" not in p.parts}
        self.assertEqual(antes, depois)

    def test_runtime_codex(self):
        self.rodar("--profile", "base", "--runtime", "codex", "--apply")
        self.assertTrue((self.proj / ".agents/skills/qa/SKILL.md").exists())

    def test_pasta_existente_nao_gerenciada_preservada(self):
        d = self.proj / ".claude/skills/qa"
        d.mkdir(parents=True)
        (d / "SKILL.md").write_text("minha versão", encoding="utf-8")
        code, res = self.rodar("--profile", "base", "--apply")
        self.assertEqual(self.status(res)["qa"], "EXISTENTE_NAO_GERENCIADA")
        self.assertEqual((d / "SKILL.md").read_text(), "minha versão")

    def test_conflito_com_edicao_local_nao_sobrescreve(self):
        self.rodar("--profile", "base", "--apply")
        f = self.proj / ".claude/skills/qa/SKILL.md"
        f.write_text("editado pelo cliente", encoding="utf-8")
        self.criar_skill("qa", "v2")
        self.gravar()
        code, res = self.rodar("--update", "--apply")
        self.assertEqual(code, 1)
        self.assertEqual(self.status(res)["qa"], "CONFLITO")
        self.assertEqual(f.read_text(), "editado pelo cliente")

    def test_atualizacao_e_rollback(self):
        self.rodar("--profile", "base", "--apply")
        self.criar_skill("qa", "v2")
        self.gravar()
        code, res = self.rodar("--check")
        self.assertEqual(self.status(res)["qa"], "ATUALIZAVEL")
        self.assertEqual((self.proj / ".claude/skills/qa/ref/notas.md").read_text(), "v1")
        code, res = self.rodar("--update", "--apply")
        self.assertEqual(self.status(res)["qa"], "ATUALIZADA_AGORA")
        self.assertEqual((self.proj / ".claude/skills/qa/ref/notas.md").read_text(), "v2")
        code, res = self.rodar("--rollback")
        self.assertEqual(self.status(res)["qa"], "REVERSAO_PREVISTA")
        self.assertEqual((self.proj / ".claude/skills/qa/ref/notas.md").read_text(), "v2")
        code, res = self.rodar("--rollback", "--apply")
        self.assertEqual(self.status(res)["qa"], "REVERTIDA")
        self.assertEqual((self.proj / ".claude/skills/qa/ref/notas.md").read_text(), "v1")
        man = json.loads((self.proj / ".lkt/instalacao.json").read_text())
        self.assertEqual(man["skills"]["qa"]["hash_origem"], "v1")

    def test_erro_parcial_restaura_estado(self):
        original = inst.shutil.copytree
        chamadas = {"n": 0}

        def copia_que_falha(src, dst, *a, **k):
            chamadas["n"] += 1
            if chamadas["n"] == 2:
                original(src, dst, *a, **k)
                raise OSError("disco cheio simulado")
            return original(src, dst, *a, **k)

        with mock.patch.object(inst.shutil, "copytree", side_effect=copia_que_falha):
            with self.assertRaises(OSError):
                inst.main(["--project", str(self.proj), "--profile", "base", "--apply"])
        self.assertFalse((self.proj / ".claude/skills/qa").exists())
        self.assertFalse((self.proj / ".claude/skills/texto-natural-pt-br").exists())
        self.assertFalse((self.proj / ".lkt/instalacao.json").exists())

    def test_perfil_invalido(self):
        code, res = self.rodar("--profile", "inexistente")
        self.assertEqual(code, 2)
        self.assertIn("perfil inexistente", res["erro"])

    def test_skill_ausente_aposentada_e_bloqueada(self):
        code, res = self.rodar("--profile", "base", "--include", "nao-existe", "--include", "salvar", "--include", "remotion-x", "--apply")
        s = self.status(res)
        self.assertEqual(s["nao-existe"], "AUSENTE")
        self.assertEqual(s["salvar"], "BLOQUEADA")
        self.assertEqual(s["remotion-x"], "BLOQUEADA")
        self.assertFalse((self.proj / ".claude/skills/salvar").exists())

    def test_nome_com_traversal_recusado(self):
        self.skills["../fora"] = {"id": "../fora", "caminho": ".claude/skills/../fora", "estado": "aprovada", "hash_arvore": "x"}
        self.gravar()
        code, res = self.rodar("--profile", "base", "--include", "../fora")
        self.assertEqual(code, 2)
        self.assertIn("nome de skill inválido", res["erro"])

    def test_destino_symlink_recusado(self):
        alvo = Path(self.tmp.name) / "outro"
        alvo.mkdir()
        (self.proj / ".claude").mkdir()
        os.symlink(alvo, self.proj / ".claude/skills")
        code, res = self.rodar("--profile", "base", "--apply")
        self.assertEqual(code, 2)
        self.assertEqual(list(alvo.iterdir()), [])

    def test_projeto_dentro_da_biblioteca_recusado(self):
        dentro = self.lib / "sub"
        dentro.mkdir()
        saida = io.StringIO()
        with contextlib.redirect_stdout(saida):
            code = inst.main(["--project", str(dentro), "--json"])
        self.assertEqual(code, 2)

    def test_projeto_inexistente(self):
        saida = io.StringIO()
        with contextlib.redirect_stdout(saida):
            code = inst.main(["--project", str(self.proj / "nao"), "--json"])
        self.assertEqual(code, 2)
        self.assertIn("projeto inexistente", saida.getvalue())

    def test_desinstalar_preserva_edicao_e_extras(self):
        self.rodar("--profile", "base", "--apply")
        (self.proj / ".claude/skills/qa/SKILL.md").write_text("editado", encoding="utf-8")
        (self.proj / ".claude/skills/texto-natural-pt-br/minhas-notas.md").write_text("meu", encoding="utf-8")
        code, res = self.rodar("--uninstall", "qa", "texto-natural-pt-br", "--apply")
        s = self.status(res)
        self.assertEqual(s["qa"], "CONFLITO")
        self.assertEqual(s["texto-natural-pt-br"], "REMOVIDA")
        self.assertTrue((self.proj / ".claude/skills/qa/SKILL.md").exists())
        self.assertTrue((self.proj / ".claude/skills/texto-natural-pt-br/minhas-notas.md").exists())
        self.assertFalse((self.proj / ".claude/skills/texto-natural-pt-br/SKILL.md").exists())

    def test_list(self):
        saida = io.StringIO()
        with contextlib.redirect_stdout(saida):
            code = inst.main(["--list"])
        self.assertEqual(code, 0)
        self.assertIn("salvar(aposentada)", saida.getvalue())


class TestRegistroReal(unittest.TestCase):
    """Confere que perfis reais só citam skills aprovadas do registro real."""

    def test_perfis_existem_e_estao_aprovados(self):
        raiz = Path(__file__).resolve().parents[1]
        regs = {r["id"]: r for r in json.loads((raiz / "registry/skills.json").read_text())["skills"]}
        perfis = json.loads((raiz / "registry/perfis.json").read_text())["perfis"]
        for nome, p in perfis.items():
            for s in p["skills"]:
                self.assertIn(s, regs, f"perfil {nome} cita {s}, ausente do registro")
                self.assertEqual(regs[s]["estado"], "aprovada", f"perfil {nome} cita {s} não aprovada")

    def test_registro_em_dia(self):
        import subprocess
        raiz = Path(__file__).resolve().parents[1]
        r = subprocess.run([sys.executable, str(raiz / "tools/registro.py"), "check", "--catalogo"], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)


if __name__ == "__main__":
    unittest.main()
