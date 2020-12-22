function verificarInicio(){
    var usuario = document.getElementById("usuarioSesion").value;
    var clave = document.getElementById("claveSesion").value;

    if ((usuario == "") || (usuario.length < 8)){
        alert("Digite su nombre de usuario");
        document.getElementById("usuarioSesion").focus();
        return false;
    }
        
    if (clave == ""){
        alert("Digite su contraseña");
        document.getElementById("claveSesion").focus();
        return false;
    }
    return true;
}

function mostrarPassword(){
    document.getElementById("claveSesion").type="text";
}
function ocultarPassword(){
    document.getElementById("claveSesion").type="password";
}

