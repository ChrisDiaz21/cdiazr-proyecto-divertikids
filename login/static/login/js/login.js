
function ButtonVisible() {
    const check = document.getElementById('id_check');
    const butt = document.getElementById('submitButton');

    // Habilitar o deshabilitar el botón dependiendo del estado del checkbox
    console.log("Checkbox estado: ", check.checked); 
    butt.disabled = !check.checked;
}


function togglePasswordVisibility() {
    var password = document.getElementById("id_password1");
    var confirmPassword = document.getElementById("id_password2");
    var mostrarContrasena = document.getElementById("mostrar_contrasena");

    if (mostrarContrasena.checked) {
        password.type = "text";
        confirmPassword.type = "text";
    } else {
        password.type = "password";
        confirmPassword.type = "password";
    }
}