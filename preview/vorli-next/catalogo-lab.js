/* VORLI Lab: progressive enhancement of reviewed, static HTML. No network calls. */
(function () {
  "use strict";
  const data = window.VORLI_CATALOG_LAB;
  const categoryRoot = document.getElementById("category-cards");
  const resourceRoot = document.getElementById("resource-cards");
  const search = document.getElementById("catalog-search");
  const select = document.getElementById("category-filter");
  const results = document.getElementById("results-count");
  const empty = document.getElementById("empty-results");
  const resetButton = document.getElementById("reset-filters");
  const emptyReset = document.getElementById("empty-reset");
  if (!categoryRoot || !resourceRoot || !search || !select || !results || !empty || !resetButton || !emptyReset) return;

  function fallback() {
    results.textContent = "Le schede restano consultabili. Ricerca e filtri temporaneamente non disponibili.";
  }
  if (!data || !Array.isArray(data.categories) || !Array.isArray(data.resources)) {
    fallback();
    return;
  }
  function norm(value) {
    return String(value || "").toLocaleLowerCase("it").normalize("NFD")
      .replace(/[\u0300-\u036f]/g, "")
      .replace(/[\u2010-\u2015\u2212/_-]+/g, " ")
      .replace(/\s+/g, " ").trim();
  }
  const categoryCards = Array.from(categoryRoot.querySelectorAll("article[data-category]"));
  const resourceCards = Array.from(resourceRoot.querySelectorAll("article[data-category]"));
  const repoBlob = "https://github.com/riccardomontanaroact-hub/affiliate-autopilot/blob/";
  const allowedSource = /^vorli\/[a-z0-9-]+\/(?:vault\/products|drafts)\/[a-zA-Z0-9._-]+\.(?:md|html)$/;
  const categorySync = categoryCards.length === data.categories.length && data.categories.every(function (c, i) {
    const heading = categoryCards[i].querySelector("h3");
    const description = categoryCards[i].querySelector("p");
    return categoryCards[i].dataset.category === c.id && heading && heading.textContent.trim() === c.name &&
      description && description.textContent.trim() === c.description;
  });
  const resourceSync = resourceCards.length === data.resources.length && data.resources.every(function (r, i) {
    const heading = resourceCards[i].querySelector("h3");
    const description = resourceCards[i].querySelector(".resource-body p");
    const link = resourceCards[i].querySelector("a[href]");
    return resourceCards[i].dataset.category === r.category && heading && heading.textContent.trim() === r.title &&
      description && description.textContent.trim() === r.description &&
      allowedSource.test(r.source) && link && link.getAttribute("href") === repoBlob + r.source;
  });
  // If editorial data and HTML disagree, preserve the visible static cards and disable filtering.
  if (!categorySync || !resourceSync) {
    fallback();
    return;
  }

  data.categories.forEach(function (c, i) {
    const option = document.createElement("option");
    option.value = c.id;
    option.textContent = c.name;
    select.appendChild(option);
    categoryCards[i].dataset.search = norm([c.name, c.description, c.keywords].join(" "));
  });
  data.resources.forEach(function (r, i) {
    resourceCards[i].dataset.search = norm([r.title, r.description, r.category].join(" "));
  });
  const cards = categoryCards.concat(resourceCards);
  function apply() {
    // Match every word, regardless of spacing or order (e.g. "casa smart").
    const terms = norm(search.value).split(/\s+/).filter(Boolean);
    const chosen = select.value;
    let categories = 0, drafts = 0;
    cards.forEach(function (card) {
      const matches = (chosen === "all" || card.dataset.category === chosen) &&
        terms.every(function (term) { return card.dataset.search.includes(term); });
      card.hidden = !matches;
      if (matches) {
        if (card.classList.contains("category")) categories++;
        else drafts++;
      }
    });
    results.textContent = categories + (categories === 1 ? " categoria demo · " : " categorie demo · ") +
      drafts + (drafts === 1 ? " risorsa in bozza visibile" : " risorse in bozza visibili");
    empty.hidden = categories + drafts !== 0;
  }
  function reset() {
    search.value = "";
    select.value = "all";
    apply();
    search.focus();
  }
  search.addEventListener("input", apply);
  select.addEventListener("change", apply);
  resetButton.addEventListener("click", reset);
  emptyReset.addEventListener("click", reset);
  document.documentElement.classList.add("js-ready");
  apply();
}());
