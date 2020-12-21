function actualizarImagen(){
    var nombreImagen = document.getElementById("nomImgActlzar").value;
    var nuevonombre = document.getElementById("nuevoNombre").value;
    var publico = document.getElementById('publicoActlzar').checked;
    var privado = document.getElementById('privadoActlzar').checked;
        
    if (nombreImagen == ""){
        alert("Debe digitar el nombre de la imagen que desea actualizar");
        document.getElementById("nomImgActlzar").focus();
        return false;
    }

    if (nuevonombre == ""){
        alert("Debe digitar el nuevo nombre de la imagen");
        document.getElementById("nuevoNombre").focus();
        return false;
    }
    
    if(!publico && !privado){
        alert("Debe seleccionar si la imagen es de tipo publica o privada");
        return false;
    } else if (publico && privado){
        alert("Seleccione un solo tipo (publica o privada)");
        return false;
    }
    return true
}