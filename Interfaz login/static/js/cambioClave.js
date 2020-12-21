function recuperarClave(){
    var correo = document.getElementById("correoRecuperar").value;

    if (correo == ""){
        alert("Debe digitar el correo al que será enviado el link de restablecimiento.");
        document.getElementById("correoRecuperar").focus();
        return false;
    }
    return true;
}