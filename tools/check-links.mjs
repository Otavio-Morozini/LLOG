#!/usr/bin/env node
/**
 * check-links.mjs — confere a saúde dos links e referências das páginas.
 *
 * Uso:  node tools/check-links.mjs
 *
 * Confere, sem acessar a internet, as PÁGINAS reais na raiz do projeto
 * (index.html, 404.html, obrigada.html):
 *  - âncoras internas (#id) que não existem na página;
 *  - href/src para arquivos locais que não estão no disco;
 *  - links wa.me / tel malformados;
 *  - marcadores [DOMINIO-QUANDO-PUBLICAR] que sobraram;
 *  - JSON de data/ inválido ou com valores ainda entre [colchetes].
 *
 * Ignora: design/ (payload do canvas), content/ (fragmentos/modelos),
 * node_modules, .git. Sem dependências.
 *
 * Saída: código 1 se houver erro; 0 se só avisos.
 */

import { readFile, readdir, access } from "node:fs/promises";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const erros = [];
const avisos = [];

const existe = (p) => access(join(ROOT, p)).then(() => true).catch(() => false);

async function paginasRaiz() {
  return (await readdir(ROOT, { withFileTypes: true }))
    .filter((e) => e.isFile() && e.name.endsWith(".html"))
    .map((e) => e.name);
}

async function checkHTML(file) {
  const html = await readFile(join(ROOT, file), "utf8");
  const ids = new Set([...html.matchAll(/\bid="([^"]+)"/g)].map((m) => m[1]));
  const refs = [...html.matchAll(/\b(?:href|src)="([^"#][^"]*)"/g)].map((m) => m[1]);
  const anchors = [...html.matchAll(/\bhref="#([^"]+)"/g)].map((m) => m[1]);

  for (const id of anchors) {
    if (id && !ids.has(id)) erros.push(`${file}: âncora #${id} não existe na página`);
  }

  for (const ref of refs) {
    if (/^(https?:|mailto:|data:)/.test(ref)) {
      if (ref.includes("wa.me/") && !/wa\.me\/(message\/[\w-]+|\d{10,15})/.test(ref)) {
        erros.push(`${file}: link wa.me suspeito -> ${ref}`);
      }
      if (ref.includes("[DOMINIO-QUANDO-PUBLICAR]")) {
        avisos.push(`${file}: URL ainda com [DOMINIO-QUANDO-PUBLICAR]`);
      }
    } else if (ref.startsWith("tel:")) {
      if (!/^tel:\+?\d{8,15}$/.test(ref)) erros.push(`${file}: tel malformado -> ${ref}`);
    } else {
      const clean = ref.split("#")[0].split("?")[0];
      if (clean && !(await existe(clean))) erros.push(`${file}: arquivo não encontrado -> ${ref}`);
    }
  }
}

async function checkJSON() {
  for (const f of await readdir(join(ROOT, "data"))) {
    if (!f.endsWith(".json")) continue;
    const raw = await readFile(join(ROOT, "data", f), "utf8");
    try {
      const obj = JSON.parse(raw);
      const ph = (JSON.stringify(obj).match(/\[[^\]]{2,}\]/g) || []).length;
      if (ph) avisos.push(`data/${f}: ${ph} valor(es) ainda entre [colchetes] a confirmar com a Hellen`);
    } catch (e) {
      erros.push(`data/${f}: JSON inválido — ${e.message}`);
    }
  }
}

const files = await paginasRaiz();
for (const f of files) await checkHTML(f);
await checkJSON();

console.log(`\n${files.length} página(s) conferida(s): ${files.join(", ")}`);
if (avisos.length) {
  console.log(`\nAVISOS (${[...new Set(avisos)].length}) — não bloqueiam, resolver antes de publicar:`);
  [...new Set(avisos)].forEach((a) => console.log("  · " + a));
}
if (erros.length) {
  console.log(`\nERROS (${[...new Set(erros)].length}):`);
  [...new Set(erros)].forEach((e) => console.log("  x " + e));
  process.exit(1);
}
console.log("\nSem erros de link. ok");
