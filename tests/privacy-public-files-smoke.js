"use strict";
/* VORLI — privacy smoke test for the draft site/preview, updated 30/10/2026.
 * Run from repository root: node tests/privacy-public-files-smoke.js
 * Standard Node.js only. Checks six selected HTML files and data/config.json.
 * Does not scan other files, Git history, deployed pages, or arbitrary encodings.
 * Do not insert real personal identifiers or affiliate tracking links in tests.
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
const encodedSeparators = /&(?:amp|#0*38|#x0*26|#0*63|#x0*3f|#0*64|#x0*40|#0*58|#x0*3a);|%(?:26|3f|3d|40|3a)/gi;
const decodeSeparator = {
  "&amp;": "&", "&#38;": "&", "&#x26;": "&",
  "&#63;": "?", "&#x3f;": "?", "&#64;": "@",
  "&#x40;": "@", "&#58;": ":", "&#x3a;": ":",
  "%26": "&", "%3f": "?", "%3d": "=", "%40": "@", "%3a": ":"
};
function normalizeForScan(source) {
  // Multiple bounded passes handle common nested &amp;amp; encodings.
  let value = source;
  for (let i = 0; i < 3; i++) {
    const next = value.replace(encodedSeparators, token => {
      const canonical = token.toLowerCase().replace(/^&#0+/, "&#").replace(/^&#x0+/, "&#x");
      return decodeSeparator[canonical] || token;
    });
    if (next === value) break;
    value = next;
  }
  return value;
}
function assertNoPrivateMarkers(source, file) {
  const normalized = normalizeForScan(source);
  if (emailPattern.test(normalized) || mailtoPattern.test(normalized)) {
    throw new Error(file + ": email address or mailto link in draft public file");
  }
  if (trackingPattern.test(normalized)) {
    throw new Error(file + ": affiliate tracking query parameter in draft public file");
  }
}
function read(relativePath) {
  return fs.readFileSync(path.join(root, relativePath), "utf8");
}
const configSource = read("data/config.json");
const config = JSON.parse(configSource);
if (typeof config.contact !== "string" || config.contact.trim() !== "") {
  throw new Error("data/config.json: draft contact must remain empty pending a compliant public channel");
}
if (typeof config.owner !== "string" || !/^VORLI\b/.test(config.owner)) {
  throw new Error("data/config.json: draft owner should be a project placeholder, not a person's name");
}
assertNoPrivateMarkers(configSource, "data/config.json");
for (const file of htmlFiles) {
  assertNoPrivateMarkers(read(file), file);
}
console.log("VORLI privacy smoke: seven draft files checked (6 HTML + config).");
console.log("Includes common HTML-entity and percent-encoded separator variants.");
console.log("Scope limited: no scan of other files, obfuscated data, live site, or Git history.");
