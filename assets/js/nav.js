/* nav.js — menu mobile + estado do header ao rolar */
(function () {
  "use strict";

  var header = document.querySelector("[data-header]");
  var toggle = document.querySelector("[data-nav-toggle]");
  var nav = document.querySelector("[data-nav]");

  if (toggle && nav) {
    var setOpen = function (open) {
      nav.dataset.open = String(open);
      toggle.setAttribute("aria-expanded", String(open));
      toggle.querySelector("[data-nav-toggle-label]") &&
        (toggle.querySelector("[data-nav-toggle-label]").textContent = open ? "Fechar" : "Menu");
    };

    toggle.addEventListener("click", function () {
      setOpen(nav.dataset.open !== "true");
    });

    nav.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        setOpen(false);
      });
    });

    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") setOpen(false);
    });

    // fecha ao voltar para desktop
    var mq = window.matchMedia("(min-width: 861px)");
    (mq.addEventListener ? mq.addEventListener.bind(mq, "change") : mq.addListener.bind(mq))(function () {
      if (mq.matches) setOpen(false);
    });
  }

  if (header) {
    var onScroll = function () {
      header.dataset.scrolled = String(window.scrollY > 8);
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }
})();
