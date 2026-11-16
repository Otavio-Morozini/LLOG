#!/usr/bin/env node
/**
 * build-pages.mjs — gera fragmentos de HTML a partir de data/*.json.
 *
 * Uso:
 *   node tools/build-pages.mjs            # gera todos os fragmentos
 *   node tools/build-pages.mjs --check    # só valida os JSON, não escreve
 *
 * Por que existe: `data/*.json` é a fonte de verdade do conteúdo. Hoje o
 * `index.html` traz o mesmo conteúdo escrito à mão (funciona sem JS e sem
 * servidor). Este script mantém as duas pontas em sincronia: escreve
 * `content/generated/portfolio.html` e `content/generated/valores.html`,
 * que o humano/próximo agente compara com o `index.html`.
 *
 * OPCIONAL — splice no lugar: se o `index.html` tiver marcadores
 *   <!-- build:portfolio:start --> ... <!-- build:portfolio:end -->
 *   <!-- build:valores:start   --> ... <!-- build:valores:end   -->
 * o script substitui o conteúdo entre eles automaticamente.
 *
 * Sem dependências.
 */

import { readFile, writeFile, mkdir } from "node:fs/promises";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const CHECK = process.argv.includes("--check");

const read = (p) => readFile(join(ROOT, p), "utf8");
const readJSON = async (p) => JSON.parse(await read(p));

function esc(s = "") {
  return String(s).replace(/&(?!amp;|lt;|gt;|#)/g, "&amp;");
}

function portfolioHTML(data) {
  const obras = data.obras
    .map((o) => {
      const cls =
        o.formato === "wide" ? "work work--wide" : o.formato === "dark" ? "work work--dark" : "work";
      return `  <article class="${cls} reveal" data-cat="${o.categoria}">
    <span class="work__kicker">${esc(o.kicker)}</span>
    <h3>${o.titulo}</h3>
    <p>${esc(o.texto)}</p>
  </article>`;
    })
    .join("\n");
  return `<!-- Gerado por tools/build-pages.mjs a partir de data/portfolio.json -->\n<div class="portfolio-grid" data-portfolio-grid>\n${obras}\n</div>\n`;
}

function precoLista(itens) {
  return itens.map((i) => `      <li>${esc(i)}</li>`).join("\n");
}

function valoresHTML(data) {
  const combos = data.combos
    .map((c) => {
      const cls = c.destaque ? "pack pack--feature" : "pack";
      const kicker = c.destaque ? `${c.kicker} · o mais pedido` : c.kicker;
      const msg = `Oi, Hellen! Vi o site e quero o ${c.kicker} — ${c.titulo} (${c.preco}). Cidade: Fraiburgo.`;
      return `  <article class="${cls} reveal">
    <span class="pack__kicker">${esc(kicker)}</span>
    <h3>${esc(c.titulo)}</h3>
    <p class="pack__price">${esc(c.preco)}</p>
    <ul>
${precoLista(c.itens)}
    </ul>
    <a class="button" href="#agenda" data-wa data-wa-msg="${esc(msg)}" data-track="${c.id}">Agendar</a>
  </article>`;
    })
    .join("\n");

  const avulsos = data.avulsos
    .map((a) => {
      const cls = a.soft ? "pack pack--soft" : "pack";
      const sufixo = a.preco_sufixo
        ? ` <span style="font-size: var(--step--1); color: var(--ink-70)">${esc(a.preco_sufixo)}</span>`
        : "";
      const aviso = a.aviso ? `\n    <p class="pack__note">${esc(a.aviso)}</p>` : "";
      const msg = `Oi, Hellen! Quero ${a.titulo} (${a.preco}).`;
      return `  <article class="${cls} reveal">
    <span class="pack__kicker">${esc(a.kicker)}</span>
    <h3>${esc(a.titulo)}${sufixo}</h3>
    <p class="pack__price">${esc(a.preco)}</p>
    <ul>
${precoLista(a.itens)}
    </ul>${aviso}
    <a class="button" href="#agenda" data-wa data-wa-msg="${esc(msg)}" data-track="${a.id}">Agendar</a>
  </article>`;
    })
    .join("\n");

  return `<!-- Gerado por tools/build-pages.mjs a partir de data/servicos.json -->\n<div class="packs" data-slot="valores.combos">\n${combos}\n${avulsos}\n</div>\n`;
}

async function splice(name, fragment) {
  const file = join(ROOT, "index.html");
  let html = await readFile(file, "utf8");
  const start = `<!-- build:${name}:start -->`;
  const end = `<!-- build:${name}:end -->`;
  const i = html.indexOf(start);
  const j = html.indexOf(end);
  if (i === -1 || j === -1) return false;
  html = html.slice(0, i + start.length) + "\n" + fragment + "        " + html.slice(j);
  if (!CHECK) await writeFile(file, html);
  return true;
}

async function main() {
  const problems = [];
  let portfolio, servicos;
  try {
    portfolio = await readJSON("data/portfolio.json");
    servicos = await readJSON("data/servicos.json");
  } catch (e) {
    console.error("JSON inválido:", e.message);
    process.exit(1);
  }

  if (!Array.isArray(portfolio.obras) || !portfolio.obras.length) problems.push("portfolio.json sem obras");
  if (!Array.isArray(servicos.combos) || !servicos.combos.length) problems.push("servicos.json sem combos");

  if (problems.length) {
    console.error("Problemas:\n - " + problems.join("\n - "));
    process.exit(1);
  }

  const frags = {
    portfolio: portfolioHTML(portfolio),
    valores: valoresHTML(servicos),
  };

  if (CHECK) {
    console.log("check ok — data/portfolio.json e data/servicos.json válidos, fragmentos montam.");
    return;
  }

  const outDir = join(ROOT, "content", "generated");
  await mkdir(outDir, { recursive: true });
  for (const [name, frag] of Object.entries(frags)) {
    await writeFile(join(outDir, `${name}.html`), frag);
    const spliced = await splice(name, frag);
    console.log(`content/generated/${name}.html escrito${spliced ? " + splice no index.html" : " (sem marcadores no index.html — só o fragmento)"}`);
  }
}

main();
