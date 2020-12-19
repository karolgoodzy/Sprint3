function actualizarImagen(){
    var nombreImagen = document.getElementById("nameImage").value;
    var nuevonombre = document.getElementById("newname").value;
        
    if (nombreImagen == ""){
        alert("Debe nombre de la imagen");
        document.getElementById("nameImage").focus();
        return false;
    } 
    if (nuevonombre == ""){
        alert("Debe el nuevo nombre de la imagen");
        document.getElementById("newname").focus();
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