// ==UserScript==
// @name         Fix Temporal Pelaez
// @namespace    https://contratistas.apelaez.com.ar/
// @version      0.1
// @description  Esto es un fix temporal al error con pantalla gris al ver estado de empleados en pelaez
// @author       David
// @match        https://contratistas.apelaez.com.ar/contratista_empleados_estado.php?codigo=1747
// @icon         https://www.google.com/s2/favicons?domain=tampermonkey.net
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

document.getElementById("large_modal").removeAttribute("class");
setTimeout(function(){
    document.getElementsByClassName("modal-backdrop fade show")[0].remove();
}, 2000);
})();