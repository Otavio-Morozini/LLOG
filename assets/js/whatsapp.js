/* whatsapp.js — monta os links wa.me a partir de atributos data-*
   Não depende de fetch (funciona em file://). A fonte de verdade das
   mensagens é data/studio.json; os textos usados aqui estão espelhados
   nos atributos data-wa-msg do HTML (tools/build-pages.mjs re-sincroniza). */
(function () {
  "use strict";

  var body = document.body;
  var numero = body.getAttribute("data-wa-number") || "";
  var linkCurto = body.getAttribute("data-wa-link") || "";

  function montaUrl(msg, prefereLinkCurto) {
    if (prefereLinkCurto && linkCurto && !msg) return linkCurto;
    if (!numero) return linkCurto || "#";
    var base = "https://wa.me/" + numero;
    return msg ? base + "?text=" + encodeURIComponent(msg) : base;
  }

  document.querySelectorAll("[data-wa]").forEach(function (a) {
    var msg = a.getAttribute("data-wa-msg") || "";
    var curto = a.hasAttribute("data-wa-curto");
    a.setAttribute("href", montaUrl(msg, curto));
    a.setAttribute("target", "_blank");
    a.setAttribute("rel", "noopener");
  });

  // Telefone (tel:) — a partir de data-tel no body
  var tel = body.getAttribute("data-tel");
  if (tel) {
    document.querySelectorAll("[data-tel-link]").forEach(function (a) {
      a.setAttribute("href", "tel:" + tel.replace(/[^\d+]/g, ""));
    });
  }
})();
