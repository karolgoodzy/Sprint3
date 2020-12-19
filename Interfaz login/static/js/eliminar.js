function eliminarImagen(){
    var nombreImagen = document.getElementById("nameImage").value;
    
    if(document.getElementById('Eliminar').checked) {
        if (nombreImagen == ""){
            alert("Debe nombre de la imagen");
            document.getElementById("nameImage").focus();
            return false;
        } 
                  
        return true;
        }
        else{
         alert("Debe seleccionar si quiere eliminar");
        document.getElementById("eliminar").focus();
         return false;
        }  
            }
