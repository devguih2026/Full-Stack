const btnDelete = document.getElementById("btnDelete");

btnDelete.addEventListener("click", function () {
    const confirmar = confirm("Tem certeza que deseja excluir esse usuário?");
    if (!confirmar) {
        console.log("Exclusão cancelada");
        return;
    }

   
    const nomeUsuario = document.getElementById("nome").value;
    const emailUsuario = document.getElementById("email").value;

    console.log("Enviando para delete:", nomeUsuario, emailUsuario);

    fetch("http://127.0.0.1:5000/Apagar", {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            nome: nomeUsuario,
            email: emailUsuario
        })
    })
    .then(response => response.json())
    .then(data => {
        alert("Usuário excluído com sucesso");
        console.log(data);
    })
    .catch(error => {
        console.error("Erro ao excluir:", error);
        alert("Erro ao excluir usuário");
    });
});
