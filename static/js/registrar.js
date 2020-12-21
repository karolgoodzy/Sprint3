function verificar(){
    var nombre = document.getElementById("nombres").value;
    var apellido = document.getElementById("apellidos").value;
    var correo = document.getElementById("correoRegistro").value;
    var usuario = document.getElementById("usuarioRegistro").value;
    var clave = document.getElementById("claveRegistro").value;
    var confirme = document.getElementById("confirme").value;

    if (nombre == ""){
        alert("Debe digitar sus nombres");
        document.getElementById("nombres").focus();
        return false;
    }

    if (apellido == ""){
        alert("Debe digitar sus apellidos");
        document.getElementById("apellidos").focus();
        return false;
    }

    if (correo == ""){
        alert("Debe digitar su correo.");
        document.getElementById("correoRegistro").focus();
        return false;
    } 

    if ((usuario == "") || (usuario.length < 8)){
        alert("El nombre de usuario debe tener mínimo 8 caracteres.");
        document.getElementById("usuarioRegistro").focus();
        return false;
    }
        
    if ((clave == "") || (clave.length < 8)){
        alert("La contraseña debe tener mínimo 8 caracteres.");
        document.getElementById("claveRegistro").focus();
        return false;
    }

    if (confirme == ""){
        alert("Confirme la contraseña");
        document.getElementById("confirme").focus();
        return false;
    }

    var n  = confirme.localeCompare(clave);
    if (n != 0 ) {
        alert("Las contraseñas no coinciden");
        document.getElementById("confirme").focus();
        return false;
        
    }

    return true;

}

function mostrarPassword1(){
    document.getElementById("claveRegistro").type="text";
}
function ocultarPassword1(){
    document.getElementById("claveRegistro").type="password";
}
function mostrarPassword2(){
    document.getElementById("confirme").type="text";
}
function ocultarPassword2(){
    document.getElementById("confirme").type="password";
}