function crearImagen(){
    var nombreImagen = document.getElementById("nomImgCrear").value;
    var publico = document.getElementById('publicoCrear').checked;
    var privado = document.getElementById('privadoCrear').checked;
    
    if (nombreImagen == ""){
        alert("Debe digitar el nombre de la imagen que desea crear");
        document.getElementById("nomImgCrear").focus();
        return false;
    }
    
    if(!publico && !privado){
        alert("Debe seleccionar si la imagen es de tipo publica o privada");
        return false;
    } else if (publico && privado){
        alert("Seleccione un solo tipo");
        return false;
    }
    return true
                          
}
        
          
    