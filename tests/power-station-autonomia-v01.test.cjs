/**
 * VORLI Power Station v0.1 — deterministic DOM-simulated regression tests.
 * Run from repository root: node tests/power-station-autonomia-v01.test.cjs
 * No dependencies, no network, no browser; does NOT certify physical-device safety.
 * Verified/test plan: 2026-10-13.
 */
"use strict";
const assert = require("node:assert/strict");
const fs = require("node:fs");
const vm = require("node:vm");
const path = require("node:path");

const source = path.join(__dirname, "..", "drafts", "power-station-autonomia-offline-2026-10-13.html");
const html = fs.readFileSync(source, "utf8");
const script = html.match(/<script>([\s\S]*?)<\/script>/i)?.[1];
assert.ok(script, "Inline JS missing");

const fields = {};
for (const name of ["capacity", "watts", "usable", "maxoutput", "variable", "model", "source", "notes"]) {
  fields[name] = { value: "", checked: false, addEventListener() {} };
}
const output = { textContent: "" };
const form = {
  elements: fields,
  reset() { for (const f of Object.values(fields)) { f.value = ""; f.checked = false; } }
};
const buttons = { print: { addEventListener() {} }, reset: { addEventListener() {} } };
const sandbox = {
  document: { getElementById(id) { return id === "form" ? form : id === "result" ? output : buttons[id]; } },
  window: { print() {} },
  confirm() { return true },
};
vm.runInNewContext(script + "\n;globalThis.__recalc = recalc;", sandbox, { timeout: 1000 });
assert.equal(typeof sandbox.__recalc, "function");
let count = 0;
function check(name, data, phrases) {
  form.reset();
  for (const [key, val] of Object.entries(data)) {
    assert.ok(fields[key], "Unknown field: " + key);
    if (key === "variable") fields[key].checked = val;
    else fields[key].value = val;
  }
  sandbox.__recalc();
  for (const phrase of phrases) assert.ok(output.textContent.includes(phrase), name + ": expected " + phrase + " in " + output.textContent);
  console.log("PASS", name);
  count++;
}
check("missing required", {}, ["Inserisci capacità"]);
check("theoretical 1000Wh / 100W", { capacity: "1000", watts: "100" }, ["10 ore", "non calcolata", "non verificato"]);
check("80 percent usable", { capacity: "1000", watts: "100", usable: "80" }, ["10 ore", "8 ore"]);
check("within continuous limit", { capacity: "1000", watts: "100", maxoutput: "500" }, ["sotto il limite"]);
check("exceeds continuous limit", { capacity: "1000", watts: "600", maxoutput: "500" }, ["ATTENZIONE: carico superiore"]);
check("variable load warning", { capacity: "1000", watts: "100", variable: true }, ["carico variabile"]);
check("negative capacity", { capacity: "-1", watts: "100" }, ["numeri positivi"]);
check("zero watts", { capacity: "1000", watts: "0" }, ["numeri positivi"]);
check("usable above 100", { capacity: "1000", watts: "100", usable: "101" }, ["Controlla fattore"]);
check("usable below zero", { capacity: "1000", watts: "100", usable: "-2" }, ["Controlla fattore"]);
check("negative output limit", { capacity: "1000", watts: "100", maxoutput: "-2" }, ["Controlla fattore"]);
check("short positive autonomy regression", { capacity: "1", watts: "1000", usable: "50" }, ["Autonomia teorica: meno di 0,01 ore", "Autonomia corretta con fattore inserito: meno di 0,01 ore"]);
check("exact 0.01 hour boundary", { capacity: "10", watts: "1000" }, ["Autonomia teorica: 0,01 ore"]);
check("decimal hours", { capacity: "750", watts: "60", usable: "90" }, ["12,5 ore", "11,25 ore"]);
check("numeric overflow", { capacity: "1e308", watts: "1e-308" }, ["Valori troppo elevati"]);
check("recalculation", { capacity: "1000", watts: "100" }, ["10 ore"]);
form.reset();
sandbox.__recalc();
assert.ok(output.textContent.includes("Inserisci capacità"), "Reset should clear result");
console.log("PASS reset"); count++;
assert.ok(html.includes('name="robots" content="noindex,nofollow"'), "Draft must remain noindex");
assert.ok(html.includes("@media print"), "Print rules missing");
assert.ok(html.includes("BOZZA · NON PUBBLICARE"), "Draft warning missing");
assert.ok(!/fetch\s*\(|XMLHttpRequest|<iframe|<script[^>]+src=/i.test(html), "External loading pattern found");
console.log("PASS static draft/offline checks");
console.log("PASS", count, "behavioral tests plus 4 static checks; DOM simulated, not a browser.");
