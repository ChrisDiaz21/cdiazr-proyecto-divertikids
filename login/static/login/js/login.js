
function ButtonVisible() {
    const check = document.getElementById('id_check');
    const butt = document.getElementById('submitButton');

    // Habilitar o deshabilitar el botón dependiendo del estado del checkbox
    console.log("Checkbox estado: ", check.checked); 
    butt.disabled = !check.checked;
}


function togglePasswordVisibility() {
    const passwords = document.querySelectorAll('input[type="password"]');
    passwords.forEach(input => {
        input.type = input.type === 'password' ? 'text' : 'password';
    });
}