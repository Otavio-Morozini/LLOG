/* agenda.js — OCIOSO até existir <div data-agenda> no HTML E o site ser servido
   por http (fetch de data/agenda.json não funciona em file://).
   Mostra uma faixa simples de disponibilidade que a Hellen atualiza à mão em
   data/agenda.json. Não cria reserva — a reserva continua no WhatsApp. */
(function () {
  "use strict";

  var alvo = document.querySelector("[data-agenda]");
  if (!alvo || typeof fetch !== "function") return;

  fetch("data/agenda.json", { cache: "no-cache" })
    .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
    .then(function (dados) {
      var semanas = (dados && dados.semanas) || [];
      var validas = semanas.filter(function (s) { return s.rotulo && s.rotulo.indexOf("[") === -1; });
      if (!validas.length) return; // ainda com placeholders — não renderiza nada

      alvo.classList.add("agenda-strip");
      alvo.innerHTML = "";
      validas.forEach(function (s) {
        var el = document.createElement("span");
        el.className = "agenda-slot";
        el.setAttribute("data-status", s.status || "livre");
        el.textContent = s.rotulo;
        alvo.appendChild(el);
      });
      if (dados.atualizado_em && dados.atualizado_em.indexOf("[") === -1) {
        var nota = document.createElement("span");
        nota.className = "agenda-slot";
        nota.style.opacity = "0.6";
        nota.textContent = "atualizado em " + dados.atualizado_em;
        alvo.appendChild(nota);
      }
    })
    .catch(function () { /* silêncio: a seção de agenda já funciona sem isto */ });
})();
