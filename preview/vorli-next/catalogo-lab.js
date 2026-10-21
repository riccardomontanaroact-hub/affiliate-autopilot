/* VORLI Lab: offline filtering of fixed, reviewed demo content. No analytics or network calls. */
(function () {
  "use strict";
  const data = window.VORLI_CATALOG_LAB;
  const categoryRoot = document.getElementById("category-cards");
  const resourceRoot = document.getElementById("resource-cards");
  const search = document.getElementById("catalog-search");
  const select = document.getElementById("category-filter");
  const results = document.getElementById("results-count");
  const empty = document.getElementById("empty-results");
  if (!data || !Array.isArray(data.categories) || !Array.isArray(data.resources)) {
    results.textContent = "Catalogo non disponibile: dati mancanti.";
    return;
  }
  function el(tag, className, text) {
    const node = document.createElement(tag);
    if (className) node.className = className;
    if (text !== undefined) node.textContent = text;
    return node;
  }
  function norm(value) {
    return String(value || "").toLocaleLowerCase("it").normalize("NFD").replace(/[\u0300-\u036f]/g, "").trim();
  }
  const categoryFragment = document.createDocumentFragment();
  const resourceFragment = document.createDocumentFragment();
  data.categories.forEach(function (c, index) {
    const option = el("option", "", c.name);
    option.value = c.id;
    select.appendChild(option);
    const card = el("article", "tile category");
    card.dataset.category = c.id;
    card.dataset.search = norm([c.name, c.description, c.keywords].join(" "));
    card.appendChild(el("span", "counter", String(index + 1).padStart(2, "0") + " / 08"));
    const icon = el("span", "glyph", c.icon);
    icon.setAttribute("aria-hidden", "true");
    card.appendChild(icon);
    card.appendChild(el("h3", "", c.name));
    card.appendChild(el("p", "", c.description));
    card.appendChild(el("span", "tag demo", "Categoria demo"));
    categoryFragment.appendChild(card);
  });
  data.resources.forEach(function (r, index) {
    const card = el("article", "tile resource");
    card.dataset.category = r.category;
    card.dataset.search = norm([r.title, r.description, r.category].join(" "));
    const cover = el("div", "cover cover-" + (index + 1));
    cover.setAttribute("aria-hidden", "true");
    cover.appendChild(el("span", "", r.cover));
    card.appendChild(cover);
    const body = el("div", "resource-body");
    body.appendChild(el("span", "tag draft", "Bozza · " + r.format));
    body.appendChild(el("h3", "", r.title));
    body.appendChild(el("p", "", r.description));
    const link = el("a", "", "Apri il file verificato su GitHub ↗");
    const allowed = /^vorli\/[a-z0-9-]+\/(?:vault\/products|drafts)\/[a-zA-Z0-9._-]+\.(?:md|html)$/;
    if (allowed.test(r.source)) {
      link.href = "https://github.com/riccardomontanaroact-hub/affiliate-autopilot/blob/" + r.source;
      link.target = "_blank";
      link.rel = "noopener noreferrer";
      body.appendChild(link);
    }
    card.appendChild(body);
    resourceFragment.appendChild(card);
  });
  // Only replace static fallback after both card collections have rendered successfully.
  categoryRoot.replaceChildren(categoryFragment);
  resourceRoot.replaceChildren(resourceFragment);
  document.documentElement.classList.add("js-ready");
  const cards = Array.from(document.querySelectorAll(".tile[data-category]"));
  function apply() {
    const query = norm(search.value);
    const chosen = select.value;
    let demo = 0, drafts = 0;
    cards.forEach(function (card) {
      const show = (chosen === "all" || card.dataset.category === chosen) &&
        norm(card.dataset.search + " " + card.textContent).includes(query);
      card.hidden = !show;
      if (show) {
        if (card.classList.contains("category")) demo++;
        else drafts++;
      }
    });
    results.textContent = demo + (demo === 1 ? " categoria demo · " : " categorie demo · ") + drafts + (drafts === 1 ? " risorsa in bozza visibile" : " risorse in bozza visibili");
    empty.hidden = (demo + drafts !== 0);
  }
  function reset() {
    search.value = "";
    select.value = "all";
    apply();
    search.focus();
  }
  search.addEventListener("input", apply);
  select.addEventListener("change", apply);
  document.getElementById("reset-filters").addEventListener("click", reset);
  document.getElementById("empty-reset").addEventListener("click", reset);
  apply();
}());
