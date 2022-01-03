// ==UserScript==
// @name         Fix Temporal Pelaez
// @namespace    https://contratistas.apelaez.com.ar/
// @version      0.2
// @description  Esto es un fix temporal al error con pantalla gris al ver estado de empleados en pelaez
// @author       David
// @match        https://contratistas.apelaez.com.ar/contratista_empleados_estado.php*
// @icon         https://www.google.com/s2/favicons?domain=tampermonkey.net
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

document.getElementById("large_modal").removeAttribute("class");
setInterval(function(){
    document.getElementsByClassName("modal-backdrop show")[0].remove();
    document.getElementsByClassName("modal-backdrop fade show")[0].remove();
}, 1000);
})();
