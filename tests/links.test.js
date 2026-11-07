// Regressão do parser de links do validador (falsos positivos do baseline de 2026-11-06).
"use strict";
const test = require("node:test");
const assert = require("node:assert");
const { extrairLinks } = require("../tools/lib/links.js");

test("link relativo real é extraído", () => {
  assert.deepStrictEqual(extrairLinks("Ver [catálogo](docs/catalogo-skills.md#topo)."), ["docs/catalogo-skills.md"]);
});

test("link entre crases é ignorado (publicar-tema, validar-sistema)", () => {
  assert.deepStrictEqual(extrairLinks("links em `[texto](url)` sempre"), []);
});

test("bloco de código cercado é ignorado (vercel/*: regex de pacotes)", () => {
  const md = "Antes\n```ts\nconst re = /[a](jsonwebtoken)/; x[0](redis|ioredis)\n```\nDepois [ok](a.md)";
  assert.deepStrictEqual(extrairLinks(md), ["a.md"]);
});

test("esquemas não-arquivo são ignorados (plugin://, http, mailto)", () => {
  const md = "[a](plugin://spreadsheets@openai-primary-runtime) [b](https://x.dev) [c](mailto:a@b.c)";
  assert.deepStrictEqual(extrairLinks(md), []);
});

test("alvos que não são caminho são ignorados ($0.00, a|b, objeto TS)", () => {
  const md = "[x]($0.00) [z](redis|ioredis) [w](data: { x: number })";
  assert.deepStrictEqual(extrairLinks(md), []);
});

test("alvo sintaticamente possível como arquivo ainda é verificado (0.0%)", () => {
  // Em conteúdo de terceiros isso vira aviso, não erro (ver validar.js).
  assert.deepStrictEqual(extrairLinks("[y](0.0%)"), ["0.0%"]);
});

test("link da raiz de um site não é tratado como arquivo do repositório", () => {
  assert.deepStrictEqual(extrairLinks("[guia](/api/docs/guides/latest-model)"), []);
});

test("caminho com espaço codificado e título é aceito", () => {
  assert.deepStrictEqual(extrairLinks('[a](minha%20pasta/x.md "título")'), ["minha pasta/x.md"]);
});

test("link quebrado real continua detectável (nano-banana-2)", () => {
  assert.deepStrictEqual(extrairLinks("Veja [edit](../nano-banana-edit)"), ["../nano-banana-edit"]);
});
