#!/usr/bin/env node
/**
 * new-section.mjs — cria o esqueleto de uma nova seção da vitrine a partir
 * de content/_MODELO-secao.html.
 *
 * Uso:
 *   node tools/new-section.mjs parcerias "Parcerias" --fundo=support
 *
 * Argumentos:
 *   1) id da seção (kebab-case)         -> vira id="parcerias"
 *   2) título entre aspas               -> vira o <h2>
 *   --fundo=support|support-soft|dark|surface  (opcional)
 *
 * Escreve content/secoes/<id>.html. Não toca no index.html — você cola o
 * bloco na posição certa e roda `node tools/check-links.mjs`.
 *
 * Sem dependências.
 */

import { readFile, writeFile, mkdir } from "node:fs/promises";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const args = process.argv.slice(2);
const id = (args[0] || "").trim();
const titulo = (args[1] || "").trim();
const fundoArg = (args.find((a) => a.startsWith("--fundo=")) || "").split("=")[1];

if (!/^[a-z][a-z0-9-]*$/.test(id) || !titulo) {
  console.error('Uso: node tools/new-section.mjs <id-kebab> "<Título>" [--fundo=support|support-soft|dark|surface]');
  process.exit(1);
}

const fundoClasse = fundoArg ? ` section--${fundoArg}` : "";

const bloco = `<!-- Seção "${titulo}" — gerada por tools/new-section.mjs.
     Cole dentro de <main> no index.html, na posição certa, e preencha os SLOT. -->
<section id="${id}" class="section${fundoClasse}">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">SLOT: olho</span>
      <h2 data-slot="${id}.titulo">${titulo}</h2>
      <p class="lead" data-slot="${id}.lead">SLOT: 1–2 frases.</p>
    </div>

    <div class="grid grid--3 reveal" data-slot="${id}.corpo">
      <article class="card">
        <h3>SLOT: item</h3>
        <p>SLOT: descrição.</p>
        <a class="text-link" href="#agenda" data-wa data-wa-msg="Oi, Hellen! SLOT.">SLOT: chamada</a>
      </article>
    </div>
  </div>
</section>
`;

const outDir = join(ROOT, "content", "secoes");
await mkdir(outDir, { recursive: true });
const outFile = join(outDir, `${id}.html`);
await writeFile(outFile, bloco);
console.log(`Escrito content/secoes/${id}.html`);
console.log(`Lembre de adicionar <a href="#${id}"> no menu (index.html) se a seção entrar na navegação.`);
