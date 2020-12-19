

function descargarImagen(){

    var nombreImagen = document.getElementById("nameImage").value;
    var usuario = document.getElementById("usuario").value;
    var clave = document.getElementById("clave").value;

        if (nombreImagen == ""){
            alert("Debe nombre de la imagen");
            document.getElementById("nameImage").focus();
            return false;
        } 
                               
        return true;
        }
       

