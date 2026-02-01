const form = document.getElementById("form");

form.addEventListener("submit", function (event) {
    event.preventDefault();

    const cep = document.getElementById("CEP").value;
    const cidade = document.getElementById("Cidade").value;
    const estado = document.getElementById("Estado").value;

    fetch("http://127.0.0.1:5000/Atualizar", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            cep: cep,
            cidade: cidade,
            estado: estado
        })
    })
    .then(response => {
        if (!response.ok) {
            return response.json().then(err => {
                throw err;
            });
        }
        return response.json();
    })
    .then(data => {
        alert("CEP cadastrado com sucesso!");
        console.log("Servidor respondeu:", data);
    })
    .catch(error => {
        alert(error.erro || "Erro ao cadastrar CEP");
        console.error("Erro:", error);
    });
});
