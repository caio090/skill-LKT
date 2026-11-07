// Gera o link "Consultar disponibilidade" de uma loja sem checkout.
// Só monta a URL: quem envia a mensagem é o cliente. Sem rede, sem envio.
"use strict";

function somenteDigitos(valor) {
  return String(valor || "").replace(/\D/g, "");
}

function montarMensagem(produto, variante) {
  const partes = [`Olá! Tem disponível o ${produto.nome}`];
  if (variante && variante.rotulo) partes.push(`(${variante.rotulo})`);
  if (variante && variante.sku) partes.push(`- SKU ${variante.sku}`);
  return partes.join(" ") + "?";
}

function montarLinkWhatsApp(numero, produto, variante) {
  const digitos = somenteDigitos(numero);
  // DDI (2) + DDD (2) + número (8 ou 9)
  if (digitos.length < 12 || digitos.length > 13) {
    throw new Error("Número inválido: use DDI + DDD + número, ex.: 55 11 90000-0000");
  }
  if (!produto || !produto.nome) throw new Error("Produto sem nome");
  return `https://wa.me/${digitos}?text=${encodeURIComponent(montarMensagem(produto, variante))}`;
}

module.exports = { montarLinkWhatsApp, montarMensagem, somenteDigitos };
