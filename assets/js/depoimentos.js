/* depoimentos.js — OCIOSO até existir <div data-depoimentos> no HTML E o site
   ser servido por http. Renderiza depoimentos reais/autorizados de
   data/depoimentos.json. Ignora itens marcados "_placeholder". */
(function () {
  "use strict";

  var alvo = document.querySelector("[data-depoimentos]");
  if (!alvo || typeof fetch !== "function") return;

  fetch("data/depoimentos.json", { cache: "no-cache" })
    .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
    .then(function (dados) {
      var itens = ((dados && dados.itens) || []).filter(function (d) {
        return d && !d._placeholder && d.texto && d.texto.indexOf("[") === -1;
      });
      if (!itens.length) return;

      alvo.classList.add("divas");
      alvo.innerHTML = "";
      itens.forEach(function (d) {
        var fig = document.createElement("figure");
        fig.className = "diva";
        var contexto = d.contexto ? " · " + d.contexto : "";
        fig.innerHTML =
          "<blockquote>&ldquo;" + escapar(d.texto) + "&rdquo;</blockquote>" +
          "<figcaption>" + escapar(d.cliente || "Cliente") + contexto + "</figcaption>";
        alvo.appendChild(fig);
      });
    })
    .catch(function () { /* silêncio: o link para o Instagram já cobre a prova social */ });

  function escapar(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c];
    });
  }
})();
