function cambiarContrasena(){
    var correo = document.getElementById("correo").value;
    var usuario = document.getElementById("usuario").value;
    var clave = document.getElementById("nuevaClave").value;
    var confirmar = document.getElementById("confirme").value;

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
        document.getElementById("nuevaClave").focus();
        return false;
    }
    var n  = confirmar.localeCompare(clave);
    
    if (n != 0 ) {
        alert("Las claves  no son iguales");
        document.getElementById("confirme").focus();
        return false;
        
    }else {
        alert("Cambio de clave realizado");
        document.getElementById("confirmar").focus();
    }

    return true;

}

function mostrarPassword(){
    document.getElementById("nuevaClave").type = "text";
}

function ocultarPassword(){
    document.getElementById("nuevaClave").type = "password";
}
function mostrarPassword2(){
    document.getElementById("confirme").type = "text";
}

function ocultarPassword2(){
    document.getElementById("confirme").type = "password";
}