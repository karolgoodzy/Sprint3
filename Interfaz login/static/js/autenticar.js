function autenticarInformacion(){
    var correo = document.getElementById("correo").value;
    var usuario = document.getElementById("usuario").value;
    var clave = document.getElementById("clave").value;
    var nombre = document.getElementById("nombre").value;
    var apellido = document.getElementById("apellido").value;
    var confirmar = document.getElementById("confirmar").value;

    if (nombre == ""){
        alert("Debe digitar colocar su nombre");
        document.getElementById("nombre").focus();
        return false;
    }

    if (apellido == ""){
        alert("Debe digitar colocar su apellido");
        document.getElementById("apellido").focus();
        return false;
    }

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
    var n  = confirmar.localeCompare(clave);
    
    if (n != 0 ) {
        alert("Las claves  no son iguales");
        document.getElementById("confirmar").focus();
        return false;
        
    }else {
        alert("usuario registrado");
        document.getElementById("confirmar").focus();
    }

    return true;

}

function mostrarPassword(){
    document.getElementById("clave").type = "text";
}

function ocultarPassword(){
    document.getElementById("clave").type = "password";
}
function mostrarPassword2(){
    document.getElementById("confirmar").type = "text";
}

function ocultarPassword2(){
    document.getElementById("confirmar").type = "password";
}