"use strict";
/* VORLI — privacy smoke test for the draft site/preview, updated 31/10/2026.
 * Run from repository root: node tests/privacy-public-files-smoke.js
 * Standard Node.js only. Checks six selected HTML files, data/config.json and the research queue.
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
const trackingPattern = /[?&](?:awc|clickref|affid|awinaffid|affiliate_id|publisher_id)=/i;
// Reject Awin click endpoints even when a publisher parameter is omitted or obscured.
const trackingEndpointPattern = /\b(?:www\.)?awin1\.com\/(?:cread|pclick|awclick|click)\.php\b/i;
const encodedSeparators = /&(?:amp|#0*(?:38|46|47|63|64|58|61)|#x0*(?:26|2e|2f|3f|40|3a|3d));|%(?:25|26|2e|2f|3f|3d|40|3a)/gi;
const decodeSeparator = {
  "&amp;": "&", "&#38;": "&", "&#x26;": "&",
  "&#63;": "?", "&#x3f;": "?", "&#64;": "@",
  "&#x40;": "@", "&#46;": ".", "&#x2e;": ".",
  "&#47;": "/", "&#x2f;": "/", "&#58;": ":", "&#x3a;": ":",
  "&#61;": "=", "&#x3d;": "=",
  "%25": "%", "%26": "&", "%2e": ".", "%2f": "/", "%3f": "?", "%3d": "=", "%40": "@", "%3a": ":"
};
function normalizeForScan(source) {
  // Multiple bounded passes handle common nested HTML entities and percent-encoding.
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
  if (trackingPattern.test(normalized) || trackingEndpointPattern.test(normalized)) {
    throw new Error(file + ": affiliate tracking query parameter in draft public file");
  }
}
// Regression fixtures use only synthetic markers, never a real affiliate identifier.
for (const fixture of [
  "?awc=synthetic",
  "?awc&#61;synthetic",
  "?awc&#x3d;synthetic",
  "?awc%3dsynthetic",
  "&amp;#63;awc&amp;#61;synthetic",
  "https://www.awin1.com/cread.php",
  "https://www.awin1.com%2fcread.php",
  "https://www.awin1&#46;com&#47;cread&#46;php",
  "https://www.awin1.com%252fcread.php",
  "?awc%253dsynthetic",
  "synthetic&#64;example&#46;invalid"
]) {
  let rejected = false;
  try { assertNoPrivateMarkers(fixture, "synthetic fixture"); }
  catch { rejected = true; }
  if (!rejected) throw new Error("Privacy scanner regression: synthetic fixture was accepted");
}
assertNoPrivateMarkers("https://example.invalid/info?topic=usb-c", "synthetic clean fixture");
assertNoPrivateMarkers("https://example.invalid/docs%2Fusb-c?topic=specs", "synthetic clean encoded fixture");
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
const researchQueueSource = read("data/product_research_queue.json");
const researchQueue = JSON.parse(researchQueueSource);
if (researchQueue.publisher_id !== null || researchQueue.affiliate_homepage_link_already_tested !== null) {
  throw new Error("Research queue must not contain publisher identifiers or tracking links");
}
assertNoPrivateMarkers(researchQueueSource, "data/product_research_queue.json");
for (const file of htmlFiles) {
  assertNoPrivateMarkers(read(file), file);
}
console.log("VORLI privacy smoke: eight draft files checked (6 HTML + config + research queue).");
console.log("Includes nested HTML-entity and percent-encoded separators, dots and slashes, plus synthetic regression fixtures.");
console.log("Scope limited: no scan of other files, obfuscated data, live site, or Git history.");
