// node --test tests/  (sem dependências, sem rede)
"use strict";
const test = require("node:test");
const assert = require("node:assert");
const path = require("path");
const fs = require("fs");
const { montarLinkWhatsApp, somenteDigitos } = require("../.claude/skills/ecommerce-loja/exemplos/link-whatsapp.js");

const catalogo = JSON.parse(fs.readFileSync(path.join(__dirname, "../.claude/skills/ecommerce-loja/exemplos/catalogo-ficticio.json"), "utf8"));

test("monta link wa.me com produto, variante e SKU codificados", () => {
  const p = catalogo.produtos[0];
  const url = montarLinkWhatsApp("+55 (00) 00000-0000", p, p.variantes[0]);
  assert.match(url, /^https:\/\/wa\.me\/5500000000000\?text=/);
  const texto = decodeURIComponent(url.split("text=")[1]);
  assert.ok(texto.includes("Tênis Corrida Modelo A"));
  assert.ok(texto.includes("SKU MODA-PRT-38"));
});

test("rejeita número sem DDI/DDD", () => {
  assert.throws(() => montarLinkWhatsApp("90000-0000", { nome: "X" }), /Número inválido/);
});

test("rejeita produto sem nome", () => {
  assert.throws(() => montarLinkWhatsApp("5500000000000", {}), /Produto sem nome/);
});

test("somenteDigitos remove formatação", () => {
  assert.strictEqual(somenteDigitos("+55 (11) 9.0000-0000"), "5511900000000");
});

test("fixtures não contêm telefone real (só zeros de exemplo)", () => {
  const telefones = JSON.stringify(catalogo).match(/\d{12,13}/g) || [];
  for (const t of telefones) assert.match(t, /^550+$/, `telefone suspeito em fixture: ${t}`);
});
