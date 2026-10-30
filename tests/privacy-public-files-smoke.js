"use strict";
/* VORLI — privacy smoke test for the draft site/preview, 30/10/2026.
 * Run from repository root: node tests/privacy-public-files-smoke.js
 * Standard Node.js only; checks seven named files, not the full repo or Git history.
 * No personal identifiers or affiliate URLs are stored in this test.
 */
const fs = require("node:fs");
const path = require("node:path");
const root = path.resolve(__dirname, "..");
const htmlFiles = [
  "site/index.html",
  "site/guida.html",
  "site/risorse.html",
  "preview/vorli-next/index.html",
  "preview/vorli-next/guida.html",
  "preview/vorli-next/risorse.html"
];
const emailPattern = /[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}/i;
const mailtoPattern = /mailto\s*:/i;
const trackingPattern = /[?&](?:awc|clickref|affid|affiliate_id|publisher_id)=/i;
function read(relativePath) {
  return fs.readFileSync(path.join(root, relativePath), "utf8");
}
const config = JSON.parse(read("data/config.json"));
if (typeof config.contact !== "string" || config.contact.trim() !== "") {
  throw new Error("data/config.json: draft contact must remain empty pending a compliant public channel");
}
if (typeof config.owner !== "string" || !/^VORLI\b/.test(config.owner)) {
  throw new Error("data/config.json: draft owner should be a project placeholder, not a person's name");
}
for (const file of htmlFiles) {
  const source = read(file);
  if (emailPattern.test(source) || mailtoPattern.test(source)) {
    throw new Error(file + ": email address or mailto link in draft public HTML");
  }
  if (trackingPattern.test(source)) {
    throw new Error(file + ": affiliate tracking query parameter in draft public HTML");
  }
}
console.log("VORLI privacy smoke: seven draft files checked (6 HTML + config).");
console.log("Scope limited: no scan of other files, encoded data, live site, or Git history.");
