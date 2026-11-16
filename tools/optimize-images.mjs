#!/usr/bin/env node
/**
 * optimize-images.mjs — prepara as fotos da Hellen para a web.
 *
 * Uso:
 *   node tools/optimize-images.mjs                 # processa assets/img/_originais/*
 *   node tools/optimize-images.mjs caminho/foto.jpg
 *
 * Com a lib `sharp` instalada (`npm i sharp` dentro de tools/), redimensiona
 * para 2000 px no maior lado, gera .webp + .jpg com qualidade ~80 e salva em
 * assets/img/. SEM sharp, o script explica o passo a passo manual e sai — não
 * quebra nada. É a peça "ociosa até haver fotos".
 *
 * Convenção de nomes: ver assets/img/README.md.
 */

import { readdir, mkdir, stat } from "node:fs/promises";
import { join, dirname, basename, extname } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const SRC_DIR = join(ROOT, "assets", "img", "_originais");
const OUT_DIR = join(ROOT, "assets", "img");
const MAX = 2000;
const QUALITY = 80;

let sharp = null;
try {
  ({ default: sharp } = await import("sharp"));
} catch {
  /* sem sharp */
}

function manual() {
  console.log(`
sharp não está instalado — modo manual.

Para instalar (opcional):
  cd tools && npm init -y && npm i sharp && cd ..
  node tools/optimize-images.mjs

Ou faça à mão (Photoshop, GIMP, Squoosh.app, Canva):
  1. Redimensione para no máx. ${MAX} px no maior lado.
  2. Exporte .webp qualidade ~${QUALITY} E um .jpg de fallback.
  3. Salve em assets/img/ com o nome da tabela em assets/img/README.md
     (ex.: assets/img/portfolio/noiva-brilho-do-sim.jpg).
  4. Peso alvo: < 250 KB por imagem.
  5. Rode: node tools/check-links.mjs
`);
}

async function processOne(file) {
  const name = basename(file, extname(file));
  const buf = sharp(file).rotate();
  const meta = await buf.metadata();
  const resize = Math.max(meta.width, meta.height) > MAX ? { width: meta.width >= meta.height ? MAX : null, height: meta.height > meta.width ? MAX : null } : null;
  const pipe = resize ? buf.resize(resize) : buf;
  await mkdir(OUT_DIR, { recursive: true });
  await pipe.clone().jpeg({ quality: QUALITY, mozjpeg: true }).toFile(join(OUT_DIR, `${name}.jpg`));
  await pipe.clone().webp({ quality: QUALITY }).toFile(join(OUT_DIR, `${name}.webp`));
  console.log(`  ${name}: .jpg + .webp gerados`);
}

async function main() {
  if (!sharp) return manual();

  const argFile = process.argv[2];
  let files = [];
  if (argFile) {
    files = [join(ROOT, argFile)];
  } else {
    const has = await stat(SRC_DIR).catch(() => null);
    if (!has) {
      console.log(`Coloque os arquivos originais em assets/img/_originais/ e rode de novo.`);
      return;
    }
    files = (await readdir(SRC_DIR))
      .filter((f) => /\.(jpe?g|png|tiff?)$/i.test(f))
      .map((f) => join(SRC_DIR, f));
  }

  if (!files.length) return console.log("Nenhuma imagem para processar.");
  console.log(`Processando ${files.length} imagem(ns) com sharp...`);
  for (const f of files) await processOne(f);
  console.log("Feito. Rode: node tools/check-links.mjs");
}

main().catch((e) => {
  console.error(e.message);
  process.exit(1);
});
