/* lightbox.js — OCIOSO até existirem âncoras [data-lightbox] no HTML.
   Quando as fotos reais entrarem no portfólio, marque cada uma:
     <a data-lightbox="portfolio" href="assets/img/portfolio/x.jpg"><img ...></a>
   e este módulo abre a galeria em tela cheia com navegação por teclado.
   Zero dependências. */
(function () {
  "use strict";

  var gatilhos = Array.prototype.slice.call(document.querySelectorAll("[data-lightbox]"));
  if (!gatilhos.length) return;

  var grupos = {};
  gatilhos.forEach(function (a, i) {
    var g = a.getAttribute("data-lightbox") || "default";
    (grupos[g] = grupos[g] || []).push(a);
    a.dataset.lbIndex = String(i);
  });

  var overlay = document.createElement("div");
  overlay.className = "lightbox";
  overlay.hidden = true;
  overlay.setAttribute("role", "dialog");
  overlay.setAttribute("aria-modal", "true");
  overlay.innerHTML =
    '<button class="lightbox__close" aria-label="Fechar">&times;</button>' +
    '<button class="lightbox__nav lightbox__nav--prev" aria-label="Anterior">&#8249;</button>' +
    '<img alt="">' +
    '<button class="lightbox__nav lightbox__nav--next" aria-label="Próxima">&#8250;</button>';
  document.body.appendChild(overlay);

  var img = overlay.querySelector("img");
  var atual = { grupo: null, i: 0 };

  function abre(grupo, i) {
    atual.grupo = grupo;
    atual.i = i;
    var a = grupos[grupo][i];
    img.src = a.getAttribute("href");
    img.alt = (a.querySelector("img") && a.querySelector("img").alt) || "";
    overlay.hidden = false;
    document.body.style.overflow = "hidden";
    overlay.querySelector(".lightbox__close").focus();
  }
  function fecha() {
    overlay.hidden = true;
    document.body.style.overflow = "";
  }
  function passo(d) {
    var arr = grupos[atual.grupo];
    abre(atual.grupo, (atual.i + d + arr.length) % arr.length);
  }

  gatilhos.forEach(function (a) {
    a.addEventListener("click", function (e) {
      e.preventDefault();
      var g = a.getAttribute("data-lightbox") || "default";
      abre(g, grupos[g].indexOf(a));
    });
  });

  overlay.querySelector(".lightbox__close").addEventListener("click", fecha);
  overlay.querySelector(".lightbox__nav--prev").addEventListener("click", function () { passo(-1); });
  overlay.querySelector(".lightbox__nav--next").addEventListener("click", function () { passo(1); });
  overlay.addEventListener("click", function (e) { if (e.target === overlay) fecha(); });
  document.addEventListener("keydown", function (e) {
    if (overlay.hidden) return;
    if (e.key === "Escape") fecha();
    if (e.key === "ArrowLeft") passo(-1);
    if (e.key === "ArrowRight") passo(1);
  });
})();
