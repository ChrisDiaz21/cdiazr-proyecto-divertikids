

function togglePasswordVisibility() {
    var password = document.getElementById("password");
    var confirmPassword = document.getElementById("confirm_password");
    var mostrarContrasena = document.getElementById("mostrar_contrasena");

    if (mostrarContrasena.checked) {
        password.type = "text";
        confirmPassword.type = "text";
    } else {
        password.type = "password";
        confirmPassword.type = "password";
    }
}
