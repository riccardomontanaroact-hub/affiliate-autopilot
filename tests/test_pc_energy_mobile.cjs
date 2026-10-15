// Run: node --test tests/test_pc_energy_mobile.cjs
// 2026-10-15: tests against tools/pc_energy_mobile.html (offline draft).
const test=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const vm=require('node:vm');
const path=require('node:path');
const html=fs.readFileSync(path.join(__dirname,'../tools/pc_energy_mobile.html'),'utf8');
const match=html.match(/<script>([\s\S]*?)<\/script>/);
assert.ok(match,'Embedded calculator script must exist');
const context={document:{getElementById:()=>({addEventListener(){}})}};
vm.createContext(context);
vm.runInContext(match[1],context);
const calc=context.estimatePcCost;
const base={active_watts:120,standby_watts:0,active_hours_per_day:4,standby_hours_per_day:0,days_per_year:220,electricity_eur_per_kwh:0.30,purchase_eur:0,maintenance_3y_eur:0};
test('desktop',()=>{const r=calc(base);assert.equal(r.total_kwh_per_year,105.6);assert.equal(r.energy_eur_per_year,31.68)});
test('laptop',()=>assert.equal(calc({...base,active_watts:45}).energy_eur_per_year,11.88));
test('standby and 3-year cost',()=>{const r=calc({...base,standby_watts:2,standby_hours_per_day:8,purchase_eur:500,maintenance_3y_eur:40});assert.equal(r.standby_kwh_per_year,3.52);assert.equal(r.energy_eur_per_year,32.74);assert.equal(r.total_eur_3_years,638.21)});
test('zero days',()=>assert.equal(calc({...base,days_per_year:0}).total_kwh_per_year,0));
test('366 days',()=>assert.equal(calc({...base,days_per_year:366}).total_kwh_per_year,175.68));
test('missing field invalid',()=>{const p={...base};delete p.active_watts;assert.throws(()=>calc(p));});
test('negative invalid',()=>assert.throws(()=>calc({...base,active_watts:-1})));
test('NaN invalid',()=>assert.throws(()=>calc({...base,electricity_eur_per_kwh:NaN})));
test('infinite invalid',()=>assert.throws(()=>calc({...base,active_watts:Infinity})));
test('overlapping hours invalid',()=>assert.throws(()=>calc({...base,active_hours_per_day:17,standby_hours_per_day:8})));
test('days over 366 invalid',()=>assert.throws(()=>calc({...base,days_per_year:367})));
test('fractional days invalid',()=>assert.throws(()=>calc({...base,days_per_year:20.5})));
test('three-year half-cent rounding agrees with Decimal',()=>{
 const r=calc({...base,active_watts:100,active_hours_per_day:1,days_per_year:10,electricity_eur_per_kwh:1.005});
 assert.equal(r.energy_eur_per_year,1.01);
 assert.equal(r.total_eur_3_years,3.02);
});


// 2026-10-15: permanent regression coverage for intermediate numeric overflow.
test('rejects annual active energy overflow',()=>{
 assert.throws(()=>calc({...base,active_watts:1e308,active_hours_per_day:24,days_per_year:366}),/Risultato troppo grande/);
});
test('rejects annual standby energy overflow',()=>{
 assert.throws(()=>calc({...base,active_hours_per_day:0,standby_watts:1e308,standby_hours_per_day:24,days_per_year:366}),/Risultato troppo grande/);
});
test('rejects total energy overflow when both subtotals are finite',()=>{
 assert.throws(()=>calc({...base,active_watts:3e307,standby_watts:3e307,active_hours_per_day:12,standby_hours_per_day:12,days_per_year:366}),/Risultato troppo grande/);
});
test('rejects annual electricity expense overflow',()=>{
 assert.throws(()=>calc({...base,electricity_eur_per_kwh:1e308}),/Risultato troppo grande/);
});
test('rejects three-year energy expense overflow',()=>{
 assert.throws(()=>calc({...base,electricity_eur_per_kwh:1e306}),/Risultato troppo grande/);
});
test('rejects total cost overflow from purchase and maintenance',()=>{
 assert.throws(()=>calc({...base,purchase_eur:1e308,maintenance_3y_eur:1e308}),/Risultato troppo grande/);
});
test('rejects cents scaling overflow for otherwise finite cost',()=>{
 assert.throws(()=>calc({...base,purchase_eur:1e307}),/Risultato troppo grande/);
});
