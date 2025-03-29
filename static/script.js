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
                    <p><strong>Género:</strong> ${data.genero}</p>
                    <p><strong>Fecha de Nacimiento:</strong> ${data.Fecha_Nacimiento}</p>
                    <p><strong>Cargo:</strong> ${data.cargo}</p>
                    <p><strong>Edad:</strong> ${data.edad}</p>
                    <img src="${data.foto}" alt="Foto de ${data.nombre}" class="mx-auto rounded-lg mt-4" style="max-width: 100%; height: auto;">
                `;
            }
        })
        .catch(error => console.error("Error:", error));
}
