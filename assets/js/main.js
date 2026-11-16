/* =========================================================================
   main.js — bootstrap da vitrine
   Estratégia: scripts clássicos (sem import/export) para funcionar tanto
   em file:// (abrir o index.html direto) quanto servido por http.
   Cada módulo em assets/js/*.js se auto-inicializa e só age se encontrar
   o seu alvo no DOM. Este arquivo apenas sinaliza que o JS está ativo.
   ========================================================================= */
(function () {
  "use strict";

  var root = document.documentElement;
  root.classList.remove("no-js");
  root.classList.add("js");

  // Ano corrente no rodapé, se houver [data-ano]
  document.querySelectorAll("[data-ano]").forEach(function (el) {
    el.textContent = String(new Date().getFullYear());
  });

  // Evento único que os módulos podem ouvir se precisarem de ordem
  document.addEventListener("DOMContentLoaded", function () {
    document.dispatchEvent(new CustomEvent("hv:ready"));
  });
})();
