function crearImagen(){
    var nombreImagen = document.getElementById("nameImage").value;
    var seleccionar = document.getElementById("seleccionar").value;
    if (nombreImagen == ""){
        alert("Debe nombre de la imagen");
        document.getElementById("nameImage").focus();
        return false;
    }         
    if (seleccionar == "") {
        alert("Debe seleccionar un archivo");
        document.getElementById("clave").focus();
        return false;
    }
    if(document.getElementById('Publica').checked){
        return true;
    } else if (document.getElementById('Privada').checked){
        return true;
    } else{
        alert("Debe seleccionar que tipo de imagen es");
        document.getElementById("clave").focus();
        return false;
    }
                          
}
        
          
    