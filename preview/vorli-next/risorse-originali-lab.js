/* VORLI Lab: preview-only original resource cards. No network requests or checkout. */
(function(){
"use strict";
var root=document.getElementById("resource-cards");
var data=window.VORLI_CATALOG_LAB;
if(!root || !data || !Array.isArray(data.resources)){if(root)root.textContent="Risorse temporaneamente non disponibili.";return;}
function el(tag,cls,value){var node=document.createElement(tag);if(cls)node.className=cls;if(value!==undefined)node.textContent=value;return node;}
var base="https://github.com/riccardomontanaroact-hub/affiliate-autopilot/blob/";
var allowed=new RegExp("^vorli/[a-z0-9-]+/(?:vault/products|drafts)/[a-zA-Z0-9._-]+[.](?:md|html)$");
data.resources.forEach(function(r,i){
 var card=el("article","tile resource");
 var cover=el("div","cover cover-"+(i+1));
 cover.setAttribute("aria-hidden","true");cover.appendChild(el("span","",r.cover));card.appendChild(cover);
 var body=el("div","resource-body");
 body.appendChild(el("span","tag draft","Bozza · "+r.format));
 body.appendChild(el("h3","",r.title));
 body.appendChild(el("p","",r.description));
 if(typeof r.source==="string" && allowed.test(r.source)){
  var link=el("a","","Esamina il file sorgente su GitHub ↗");
  link.href=base+r.source;link.target="_blank";link.rel="noopener noreferrer";
  body.appendChild(link);
 }else{body.appendChild(el("p","","Sorgente non verificato: collegamento disabilitato."));}
 card.appendChild(body);root.appendChild(card);
});
}());