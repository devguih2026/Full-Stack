const form = document.getElementById("form"); // acessa o <form id="form"> do HTML

form.addEventListener("submit", function (event) {
    event.preventDefault(); // impede recarregar a página, Sem isso, o navegador recarrega a página e mata a comunicação
 
    // Pega os valores dos inputs
    const nome = document.getElementById("nome").value;  // .value pega o que o usuário digitou
    const email = document.getElementById("email").value;

    fetch("http://127.0.0.1:5000/Atualizar", { // fetch() = Postman do navegador.
        method: "PUT",
        headers: {
            "Content-Type": "application/json"  // enviando JSON
        },
        body: JSON.stringify({ // Transforma objeto JS em JSON
            nome: nome,
            email: email
        })
    })
    .then(response => response.json()) // Converte a resposta do Flask em objeto JS
    .then(data => { // Aqui você recebe o retorno do back-end
        alert("Email alterado");
        console.log(data);
    })
    .catch(error => {
        console.error("Erro:", error);
    });
});
