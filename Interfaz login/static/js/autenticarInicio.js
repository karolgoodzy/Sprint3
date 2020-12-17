function autenticarInicio(){
    var correo = document.getElementById("correo").value;
    var usuario = document.getElementById("usuario").value;
    var clave = document.getElementById("clave").value;


    if (correo == ""){
        alert("Debe digitar el correo.");
        document.getElementById("correo").focus();
        return false;
    } 

    if ((usuario == "") || (usuario.length < 8)){
        alert("El usuario debe tener mínimo 8 caracteres.");
        document.getElementById("usuario").focus();
        return false;
    }
        
    if ((clave == "") || (clave.length < 8)){
        alert("La clave debe tener mínimo 8 caracteres.");
        document.getElementById("clave").focus();
        return false;
    }
    return true;
    }

function actualizarCrear(){
    var nombreImagen = document.getElementById("nameImage").value;
    var nuevonombre = document.getElementById("newname").value;
    var usuario = document.getElementById("usuario").value;
    var clave = document.getElementById("clave").value;
    var seleccionar = document.getElementById("seleccionar").value;
    if(document.getElementById('Actualizar').checked) {
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
        if ((usuario == "") || (usuario.length < 8)){
            alert("El usuario debe tener mínimo 8 caracteres.");
            document.getElementById("usuario").focus();
            return false;
        }
            
        if ((clave == "") || (clave.length < 8)){
            alert("La clave debe tener mínimo 8 caracteres.");
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
        if (document.getElementById('Crear').checked) {
            if (nombreImagen == ""){
                alert("Debe nombre de la imagen");
                document.getElementById("nameImage").focus();
                return false;
             }         
            if ((usuario == "") || (usuario.length < 8)){
                alert("El usuario debe tener mínimo 8 caracteres.");
                document.getElementById("usuario").focus();
                return false;
            }
            
            if ((clave == "") || (clave.length < 8)){
                alert("La clave debe tener mínimo 8 caracteres.");
                document.getElementById("clave").focus();
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
            return true;                
        }
        else{
            alert("Debe seleccionar que quiere hacer");
            document.getElementById("clave").focus();
            return false;
        }  
    }