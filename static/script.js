function buscarPersona() {
    let cedula = document.getElementById("cedula").value;

    fetch(`/buscar?cedula=${cedula}`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                document.getElementById("resultado").innerHTML = `<p style="color:red">${data.error}</p>`;
            } else {
                document.getElementById("resultado").innerHTML = `
                    <p><strong>Nombre:</strong> ${data.nombre} ${data.apellido}</p>
                    <p><strong>Edad:</strong> ${data.edad}</p>
                `;
            }
        })
        .catch(error => console.error("Error:", error));
}
