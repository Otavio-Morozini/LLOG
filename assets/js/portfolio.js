/* portfolio.js — filtro do portfólio por categoria (opera sobre o DOM já renderizado) */
(function () {
  "use strict";

  var filtros = document.querySelector("[data-portfolio-filters]");
  var grade = document.querySelector("[data-portfolio-grid]");
  if (!filtros || !grade) return;

  var botoes = filtros.querySelectorAll("button[data-filter]");
  var obras = grade.querySelectorAll("[data-cat]");

  function aplicar(cat) {
    botoes.forEach(function (b) {
      b.setAttribute("aria-pressed", String(b.dataset.filter === cat));
    });
    obras.forEach(function (obra) {
      var mostra = cat === "todos" || obra.dataset.cat === cat;
      obra.hidden = !mostra;
    });
    // Atualiza o hash sem pular a página (permite compartilhar um filtro)
    if (history.replaceState) {
      history.replaceState(null, "", cat === "todos" ? location.pathname + location.search : "#portfolio=" + cat);
    }
  }

  botoes.forEach(function (b) {
    b.addEventListener("click", function () { aplicar(b.dataset.filter); });
  });

  // Estado inicial a partir do hash (#portfolio=noiva)
  var m = /portfolio=([a-z-]+)/.exec(location.hash);
  aplicar(m ? m[1] : "todos");
})();
