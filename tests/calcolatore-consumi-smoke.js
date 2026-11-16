"use strict";
/* VORLI — smoke test offline del calcolatore, 29/10/2026.
 * Eseguire: node tests/calcolatore-consumi-smoke.js
 * Solo Node.js standard, nessuna rete. DOM simulato: NON equivale a test browser.
 */
function runSmokeTests(html) {
  const match = html.match(/<script>([\s\S]*?)<\/script>/);
  if (!match) throw new Error("Script incorporato non trovato");
  const passed = [];
  function check(label, condition) {
    if (!condition) throw new Error("FAIL: " + label);
    passed.push(label);
  }
  let csvText = null, downloadClicks = 0, printCalls = 0;
  class FakeElement {
    constructor(id) {
      this.id = id; this.value = ""; this.textContent = "";
      this.disabled = false; this.children = []; this.listeners = {};
    }
    addEventListener(type, listener) { this.listeners[type] = listener; }
    dispatch(type) {
      if (!this.listeners[type]) throw new Error("Listener mancante: " + type);
      this.listeners[type]({ preventDefault() {} });
    }
    replaceChildren() { this.children = []; }
    appendChild(child) { this.children.push(child); }
    remove() {}
    click() { downloadClicks++; }
  }
  const ids = ["calculator", "results", "error", "status", "csv", "print", "price"];
  for (let i = 1; i <= 3; i++) {
    for (const prefix of ["name", "watts", "hours", "days"]) ids.push(prefix + i);
  }
  const elements = Object.fromEntries(ids.map(id => [id, new FakeElement(id)]));
  const document = {
    getElementById(id) {
      if (!elements[id]) throw new Error("Elemento non simulato: " + id);
      return elements[id];
    },
    createElement(tag) { return new FakeElement(tag); },
    body: { appendChild() {} }
  };
  class FakeBlob { constructor(parts) { csvText = parts.join(""); } }
  const fakeURL = {
    createObjectURL() { return "blob:mock"; },
    revokeObjectURL() {}
  };
  new Function("document", "window", "Blob", "URL", "setTimeout", match[1])(
    document, { print() { printCalls++; } }, FakeBlob, fakeURL, fn => fn()
  );
  function put(id, value) {
    elements[id].value = String(value);
    elements.calculator.dispatch("input");
  }
  function submit() { elements.calculator.dispatch("submit"); }
  function cell(row, column) {
    return elements.results.children[row].children[column].textContent;
  }
  put("price", "0,25");
  put("watts1", "100"); put("hours1", "8"); put("days1", "365");
  submit();
  check("una riga calcolata", elements.results.children.length === 1);
  check("energia 292,00 kWh", cell(0, 1) === "292,00");
  check("costo 73,00 euro", cell(0, 2) === "73,00");
  check("media mensile 6,08 euro", cell(0, 3) === "6,08");
  check("CSV abilitato", elements.csv.disabled === false);
  put("price", "0,30");
  check("tabella invalidata dopo modifica", elements.results.children.length === 0);
  check("CSV disabilitato dopo modifica", elements.csv.disabled === true);
  submit();
  check("ricalcolo tariffa 87,60 euro", cell(0, 2) === "87,60");
  put("name1", '=1+1;\n"x"');
  submit(); elements.csv.dispatch("click");
  check("CSV neutralizza formula e virgolette", csvText.includes('"Nome: =1+1; ""x"""'));
  check("download locale invocato", downloadClicks === 1);
  put("hours1", "25"); submit();
  check("ore oltre 24 rifiutate", elements.error.textContent.includes("Dispositivo 1") && elements.csv.disabled);
  put("hours1", "8"); put("days1", "365,5"); submit();
  check("giorni frazionari rifiutati", elements.error.textContent.includes("Dispositivo 1"));
  put("days1", "365"); put("watts2", "50"); put("hours2", "4"); put("days2", "200");
  submit();
  check("due dispositivi confrontati", elements.results.children.length === 2);
  check("secondo dispositivo 40,00 kWh", cell(1, 1) === "40,00");
  elements.print.dispatch("click");
  check("stampa invocata", printCalls === 1);
  elements.calculator.dispatch("reset");
  check("reset pulisce risultati e CSV", elements.results.children.length === 0 && elements.csv.disabled);
  return { passed: passed.length, checks: passed };
}
if (typeof module !== "undefined") {
  module.exports = { runSmokeTests };
  if (require.main === module) {
    const fs = require("node:fs");
    const path = require("node:path");
    const file = path.resolve(__dirname, "../products/drafts/2026-10-29-calcolatore-consumi-offline.html");
    const result = runSmokeTests(fs.readFileSync(file, "utf8"));
    console.log("VORLI calcolatore: " + result.passed + " controlli DOM simulati superati.");
  }
}
