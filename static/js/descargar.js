function descargarImagen(){
    var nombreImagen = document.getElementById("nomImgDescgar").value;

    if (nombreImagen == ""){
        alert("Debe digitar el nombre de la imagen a descargar");
        document.getElementById("nomImgDescgar").focus();
        return false;
    }
    return true;
}