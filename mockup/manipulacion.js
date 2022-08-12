
let boton = document.querySelector('button');

function show_resultado(){

    let tamanio = document.querySelector("input#tamanio").value
    let cuartos = document.querySelector("input#cuartos").value
    let flag_banio = document.querySelector("select#banios").value

    
    let pred = parseInt(tamanio*2) + parseInt(cuartos)
    if (flag_banio==1){
        pred = pred*1.5
        alert(pred)
    }

    const target = document.getElementById("resultado-prediccion")
    target.innerHTML=pred
    
}


boton.addEventListener('click', show_resultado);