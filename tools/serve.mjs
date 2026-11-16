#!/usr/bin/env node
/**
 * serve.mjs — servidor estático local, zero dependências.
 *
 * Uso:
 *   node tools/serve.mjs [porta] [raiz]
 *   node tools/serve.mjs 4173 .
 *
 * Por que existe: a vitrine é HTML/CSS/JS puro e deve rodar sem build.
 * Este servidor permite testar `fetch()` de `data/*.json` (que falha em file://)
 * e conferir a página no navegador com um endereço http real.
 *
 * Não entra "no ar" em produção — em produção basta publicar a pasta num
 * host estático (GitHub Pages, Netlify, Cloudflare Pages). Fica aqui pronto
 * para o desenvolvimento e para o próximo agente.
 */

import { createServer } from "node:http";
import { readFile, stat } from "node:fs/promises";
import { join, extname, normalize, resolve, sep } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = resolve(process.argv[3] ?? join(fileURLToPath(new URL(".", import.meta.url)), ".."));
const PORT = Number(process.argv[2] ?? process.env.PORT ?? 4173);

const MIME = {
  ".html": "text/html; charset=utf-8",
  ".css": "text/css; charset=utf-8",
  ".js": "text/javascript; charset=utf-8",
  ".mjs": "text/javascript; charset=utf-8",
  ".json": "application/json; charset=utf-8",
  ".svg": "image/svg+xml",
  ".png": "image/png",
  ".jpg": "image/jpeg",
  ".jpeg": "image/jpeg",
  ".webp": "image/webp",
  ".avif": "image/avif",
  ".ico": "image/x-icon",
  ".woff2": "font/woff2",
  ".woff": "font/woff",
  ".ttf": "font/ttf",
  ".txt": "text/plain; charset=utf-8",
  ".webmanifest": "application/manifest+json",
};

const server = createServer(async (req, res) => {
  try {
    const url = new URL(req.url, `http://${req.headers.host}`);
    let pathname = decodeURIComponent(url.pathname);
    if (pathname.endsWith("/")) pathname += "index.html";

    // impede path traversal
    const target = normalize(join(ROOT, pathname));
    if (!target.startsWith(ROOT + sep) && target !== ROOT) {
      res.writeHead(403).end("403 — fora da raiz");
      return;
    }

    let filePath = target;
    let info = await stat(filePath).catch(() => null);
    if (info?.isDirectory()) {
      filePath = join(filePath, "index.html");
      info = await stat(filePath).catch(() => null);
    }

    if (!info) {
      // fallback: 404.html na identidade da marca, se existir
      const notFound = join(ROOT, "404.html");
      const has404 = await stat(notFound).catch(() => null);
      if (has404) {
        res.writeHead(404, { "content-type": MIME[".html"] });
        res.end(await readFile(notFound));
      } else {
        res.writeHead(404, { "content-type": "text/plain; charset=utf-8" });
        res.end("404 — nao encontrado");
      }
      return;
    }

    const body = await readFile(filePath);
    res.writeHead(200, {
      "content-type": MIME[extname(filePath).toLowerCase()] ?? "application/octet-stream",
      "cache-control": "no-cache",
    });
    res.end(body);
  } catch (err) {
    res.writeHead(500, { "content-type": "text/plain; charset=utf-8" });
    res.end("500 — " + err.message);
  }
});

server.listen(PORT, () => {
  console.log(`Studio Hellen Varella — servidor local`);
  console.log(`  raiz: ${ROOT}`);
  console.log(`  http://127.0.0.1:${PORT}/`);
});
