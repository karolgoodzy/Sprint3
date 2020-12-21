function habilitar(){
    var checkeado = document.getElementById('checkborrar').checked
    if (checkeado){
        document.getElementById('eliminar').disabled = false
        document.getElementById('nomImgElimnar').disabled = false
    } else {
        document.getElementById('eliminar').disabled = true
        document.getElementById('nomImgElimnar').disabled = true
    }
}

function eliminarImagen(){
    var nombreImagen = document.getElementById("nomImgElimnar").value;
    
    if(document.getElementById('checkborrar').checked) {
        if (nombreImagen == ""){
            alert("Debe digitar el nombre de la imagen que quiere borrar");
            document.getElementById("nomImgElimnar").focus();
            return false;
        }
    }
    return true;
}