// Extração de links Markdown verificáveis (caminhos relativos do repositório).
// Ignora código (blocos cercados e `inline`), URLs com esquema (http:, mailto:,
// plugin:, data: ...), links da raiz de um site (/api/...) e alvos que não
// podem ser caminho de arquivo (espaços, |, $, chaves).
"use strict";

function removerCodigo(texto) {
  // blocos cercados ``` ou ~~~ (fechamento com a mesma cerca)
  let semBlocos = texto.replace(/^([ \t]*)(`{3,}|~{3,})[^\n]*\n[\s\S]*?^\1?\2[ \t]*$/gm, "");
  // blocos não fechados até o fim do arquivo
  semBlocos = semBlocos.replace(/^[ \t]*(`{3,}|~{3,})[^\n]*\n[\s\S]*$/m, "");
  // código inline com 1+ crases balanceadas
  return semBlocos.replace(/(`+)[^`\n]*?\1/g, "");
}

function ehCaminhoVerificavel(alvo) {
  if (!alvo) return false;
  if (/^[a-z][a-z0-9+.-]*:/i.test(alvo)) return false; // esquema: http:, plugin:, mailto:...
  if (alvo.startsWith("/")) return false; // raiz de site, não do repositório
  if (alvo.startsWith("#")) return false; // âncora local
  if (/[\s|${}<>]/.test(alvo)) return false; // não é caminho de arquivo
  return true;
}

function extrairLinks(texto) {
  const limpo = removerCodigo(texto);
  const links = [];
  const padrao = /\]\(\s*(<[^>]*>|[^)\s]+)(?:\s+"[^"]*")?\s*\)/g;
  let m;
  while ((m = padrao.exec(limpo))) {
    const bruto = m[1].replace(/^<|>$/g, "").split("#")[0].trim();
    if (!ehCaminhoVerificavel(bruto)) continue;
    let alvo = bruto;
    try {
      alvo = decodeURI(bruto);
    } catch (e) {
      /* mantém o original */
    }
    links.push(alvo);
  }
  return links;
}

module.exports = { extrairLinks, removerCodigo, ehCaminhoVerificavel };
