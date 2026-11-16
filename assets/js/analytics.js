/* analytics.js — OCIOSO / opt-in. Medição sem cookies, sem terceiros, sem
   dados pessoais. Só conta cliques em CTAs (WhatsApp, telefone, combos) e
   filtros de portfólio, para a Hellen saber o que puxa contato.

   Desligado por padrão. Para ligar, defina no HTML antes deste script:
     <script>window.HV_ANALYTICS = { endpoint: "https://SEU-COLETOR/evento" };</script>
   Sem endpoint, os eventos só aparecem no console (útil em teste).
   Respeita navigator.doNotTrack / globalPrivacyControl. */
(function () {
  "use strict";

  var cfg = window.HV_ANALYTICS || {};
  var dnt = navigator.doNotTrack === "1" || window.doNotTrack === "1" || navigator.globalPrivacyControl === true;
  if (dnt && !cfg.ignoreDNT) return;

  function envia(nome, dados) {
    var payload = Object.assign({ evento: nome, pagina: location.pathname, ts: Date.now() }, dados || {});
    if (cfg.endpoint && navigator.sendBeacon) {
      try { navigator.sendBeacon(cfg.endpoint, JSON.stringify(payload)); } catch (e) {}
    }
    if (!cfg.endpoint || cfg.debug) {
      // eslint-disable-next-line no-console
      console.info("[hv:evento]", payload);
    }
  }

  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest("a, button");
    if (!a) return;

    if (a.matches("[data-wa]") || (a.href && a.href.indexOf("wa.me") > -1)) {
      envia("whatsapp_click", { rotulo: (a.textContent || "").trim().slice(0, 40) });
    } else if (a.matches("[data-tel-link]") || (a.href && a.href.indexOf("tel:") === 0)) {
      envia("telefone_click");
    } else if (a.matches("[data-filter]")) {
      envia("portfolio_filtro", { filtro: a.dataset.filter });
    } else if (a.matches("[data-combo-cta]")) {
      envia("combo_montado");
    } else if (a.matches("[data-track]")) {
      envia("cta_click", { rotulo: a.dataset.track });
    }
  }, true);

  envia("pageview");
})();
