"use strict";
const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

const root = path.resolve(__dirname, "..");
const dir = path.join(root, "preview", "vorli-next");
const html = fs.readFileSync(path.join(dir, "catalogo-lab.html"), "utf8");
const css = fs.readFileSync(path.join(dir, "catalogo-lab.css"), "utf8");
const js = fs.readFileSync(path.join(dir, "catalogo-lab.js"), "utf8");
const context = { window: {} };
vm.runInNewContext(fs.readFileSync(path.join(dir, "catalogo-lab-data.js"), "utf8"), context);
const data = context.window.VORLI_CATALOG_LAB;
const repoBlob = "https://github.com/riccardomontanaroact-hub/affiliate-autopilot/blob/";

test("Eight category and five draft cards are present without JavaScript", () => {
  assert.equal((html.match(/<article class="tile category"/g) || []).length, 8);
  assert.equal((html.match(/<article class="tile resource"/g) || []).length, 5);
  assert.match(html, /name="robots" content="noindex,nofollow"/);
  assert.match(html, /href="catalogo-statico-lab\.html"/);
  assert.match(html, /La ricerca richiede JavaScript/);
  assert.doesNotMatch(html, /<form\b|type="submit"|href="[^"]*(?:checkout|payment)/i);
});

test("Catalog data and static editorial cards agree", () => {
  assert.equal(data.categories.length, 8);
  assert.equal(data.resources.length, 5);
  assert.equal(data.commercialOffers, 0);
  assert.equal(data.checkoutEnabled, false);
  assert.equal(data.publicationApproved, false);
  for (const category of data.categories) {
    assert.ok(html.includes('data-category="' + category.id + '"'));
    assert.ok(html.includes("<h3>" + category.name + "</h3>"));
    assert.ok(html.includes("<p>" + category.description + "</p>"), "category description: " + category.name);
  }
  for (const resource of data.resources) {
    assert.ok(html.includes(resource.title.replaceAll("&", "&amp;")));
    assert.ok(html.includes("<p>" + resource.description + "</p>"), "resource description: " + resource.title);
    assert.ok(html.includes(repoBlob + resource.source + '"'));
    assert.match(resource.source, /^vorli\/[a-z0-9-]+\/(?:vault\/products|drafts)\/[a-zA-Z0-9._-]+\.(?:md|html)$/);
  }
});

test("Hydration filters existing HTML instead of replacing it", () => {
  assert.match(js, /categoryRoot\.querySelectorAll\("article\[data-category\]"\)/);
  assert.match(js, /resourceRoot\.querySelectorAll\("article\[data-category\]"\)/);
  assert.match(js, /categorySync/);
  assert.match(js, /resourceSync/);
  assert.match(js, /description\.textContent\.trim\(\) === c\.description/);
  assert.match(js, /description\.textContent\.trim\(\) === r\.description/);
  assert.match(js, /if \(!categorySync \|\| !resourceSync\)/);
  assert.match(js, /card\.hidden = !matches/);
  assert.match(js, /split\(\/\\s\+\/\)\.filter\(Boolean\)/);
  assert.match(js, /terms\.every\(/);
  assert.ok(js.includes("replace(/[\\u2010-\\u2015\\u2212/_-]+/g, \" \")"), "normalize dash/slash separators");
  assert.match(html, /role="search" aria-label="Ricerca e filtri del catalogo demo"/);
  assert.equal((html.match(/aria-controls="category-cards resource-cards"/g) || []).length, 2);
  assert.doesNotMatch(js, /replaceChildren\s*\(|innerHTML\s*=/);
  assert.match(js, /classList\.add\("js-ready"\)/);
  assert.match(css, /\.filters\{display:none/);
  assert.match(css, /\.js-ready \.filters\{display:grid/);
  assert.match(css, /@media\(forced-colors:active\)/);
  assert.match(css, /@media\(prefers-contrast:more\)/);
});

test("Internal links in all Lab pages resolve to repository files", () => {
  for (const filename of ["catalogo-lab.html", "catalogo-statico-lab.html", "risorse-originali-lab.html", "guida-scelta-tech-lab.html"]) {
    const page = fs.readFileSync(path.join(dir, filename), "utf8");
    for (const match of page.matchAll(/href="([^"]+)"/g)) {
      const href = match[1];
      if (/^(?:https?:|mailto:|#)/.test(href)) continue;
      const target = href.split("#")[0].split("?")[0];
      if (target) assert.ok(fs.existsSync(path.join(dir, target)), filename + " → " + target + " missing");
    }
  }
});

test("External links in catalog are only registered original GitHub sources", () => {
  const external = Array.from(html.matchAll(/href="(https?:\/\/[^"]+)"/g), m => m[1]).sort();
  const registered = Array.from(data.resources, r => repoBlob + r.source).sort();
  assert.deepEqual(external, registered);
  assert.doesNotMatch(html + js + css, /<iframe\b|<script[^>]+src="https?:\/\//i);
});

test("Eight category cards link to an original, noindex buying-criteria guide", () => {
  const guide = fs.readFileSync(path.join(dir, "guida-scelta-tech-lab.html"), "utf8");
  assert.match(guide, /name="robots" content="noindex,nofollow"/);
  assert.match(guide, /href="catalogo-lab.css"/);
  assert.equal((guide.match(/class="tile guide-card"/g) || []).length, 8);
  assert.equal((html.match(/class="category-link"/g) || []).length, 8);
  for (const forbidden of ["<script", "<form", "<iframe", "https://", "http://"]) assert.ok(!guide.toLowerCase().includes(forbidden), forbidden);
  assert.ok(css.includes(".guide-grid{"));
  for (const category of data.categories) {
    assert.ok(html.includes('href="guida-scelta-tech-lab.html#' + category.id + '"'));
    assert.ok(guide.includes('id="' + category.id + '"'));
    assert.ok(guide.includes('href="#' + category.id + '"'));
    assert.ok(guide.includes('<h3 id="' + category.id + '-title">' + category.name + '</h3>'));
  }
});

