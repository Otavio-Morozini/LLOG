/* pricing.js — "Montar meu combo": a cliente marca o que quer e vê qual
   combo corresponde e o preço. Opera sobre o bloco [data-combo-builder]
   já presente no HTML (as opções e a tabela vêm de data-* — sem fetch). */
(function () {
  "use strict";

  var box = document.querySelector("[data-combo-builder]");
  if (!box) return;

  var chips = box.querySelectorAll("[data-combo-opt]");
  var saida = box.querySelector("[data-combo-result]");
  var cta = box.querySelector("[data-combo-cta]");

  // Mapa de combinações -> combo. Chave = conjunto ordenado de opções.
  var TABELA = {
    "make": { nome: "Combo 1 — Maquiagem + ensaio", preco: "R$ 300" },
    "cabelo|make": { nome: "Combo 2 — Maquiagem + cabelo + ensaio", preco: "R$ 370" },
    "cabelo|look|make": { nome: "Combo 3 — Produção completa + ensaio", preco: "R$ 420" },
    "": { nome: "Combo 4 — Só ensaio fotográfico", preco: "R$ 260" }
  };

  function estado() {
    var sel = [];
    chips.forEach(function (c) {
      if (c.getAttribute("aria-pressed") === "true") sel.push(c.dataset.comboOpt);
    });
    return sel.sort().join("|");
  }

  function atualiza() {
    var chave = estado();
    var combo = TABELA[chave];
    if (!combo) {
      // fallback: sobe para a combinação mais próxima
      combo = chave.indexOf("cabelo") > -1 ? TABELA["cabelo|make"] : TABELA["make"];
    }
    saida.innerHTML = "Seu combo: <strong>" + combo.preco + "</strong> · " + combo.nome;
    if (cta) {
      var msg = "Oi, Hellen! Vi o site e quero o " + combo.nome + " (" + combo.preco + "). Cidade: Fraiburgo.";
      var numero = document.body.getAttribute("data-wa-number") || "";
      cta.setAttribute("href", numero ? "https://wa.me/" + numero + "?text=" + encodeURIComponent(msg) : "#");
    }
  }

  chips.forEach(function (c) {
    c.addEventListener("click", function () {
      var on = c.getAttribute("aria-pressed") === "true";
      c.setAttribute("aria-pressed", String(!on));
      atualiza();
    });
  });

  box.hidden = false;
  atualiza();
})();
