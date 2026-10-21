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

test("Static HTML works as editorial fallback without JavaScript", () => {
  assert.equal((html.match(/<article class="tile category"/g) || []).length, 8);
  assert.equal((html.match(/<article class="tile resource"/g) || []).length, 5);
  assert.match(html, /noindex,nofollow/);
  assert.match(html, /catalogo-statico-lab\.html/);
  assert.match(html, /La ricerca richiede JavaScript/);
  assert.doesNotMatch(html, /<form\b|type="submit"|href="[^"]*(?:checkout|payment)/i);
});

test("Demo and draft data are explicit and correspond to fallback cards", () => {
  assert.equal(data.categories.length, 8);
  assert.equal(data.resources.length, 5);
  assert.equal(data.commercialOffers, 0);
  assert.equal(data.checkoutEnabled, false);
  assert.equal(data.publicationApproved, false);
  for (const category of data.categories) {
    assert.ok(html.includes(`data-category="${category.id}"`));
  }
  for (const resource of data.resources) {
    assert.ok(html.includes(resource.title.replaceAll("&", "&amp;")));
    assert.ok(html.includes(`/blob/${resource.source}"`));
    assert.match(resource.source, /^vorli\/[a-z0-9-]+\/(?:vault\/products|drafts)\/[a-zA-Z0-9._-]+\.(?:md|html)$/);
  }
});

test("JavaScript enhances only after both fragments are ready", () => {
  assert.match(js, /categoryFragment = document\.createDocumentFragment\(\)/);
  assert.match(js, /resourceFragment = document\.createDocumentFragment\(\)/);
  assert.match(js, /categoryRoot\.replaceChildren\(categoryFragment\)/);
  assert.match(js, /resourceRoot\.replaceChildren\(resourceFragment\)/);
  assert.match(js, /classList\.add\("js-ready"\)/);
  assert.match(css, /\.filters\{display:none/);
  assert.match(css, /\.js-ready \.filters\{display:grid/);
});

test("Internal page links in Lab HTML have local targets", () => {
  for (const filename of ["catalogo-lab.html", "catalogo-statico-lab.html", "risorse-originali-lab.html"]) {
    const page = fs.readFileSync(path.join(dir, filename), "utf8");
    for (const match of page.matchAll(/href="([^"]+)"/g)) {
      const href = match[1];
      if (/^(?:https?:|mailto:|#)/.test(href)) continue;
      const target = href.split("#")[0].split("?")[0];
      if (!target) continue;
      assert.ok(fs.existsSync(path.join(dir, target)), `${filename} → ${target} missing`);
    }
  }
});
