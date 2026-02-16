const form = document.getElementById("Form");
const cpfInput = document.getElementById("cpf");
const senhaInput = document.getElementById("senha");

form.addEventListener("submit", async function (event) {
    event.preventDefault();

    const cpf = cpfInput.value.trim();
    const senha = senhaInput.value.trim();

    if (cpf === "" || senha === "") {
        alert("Preencha todos os campos.");
        return;
    }

    if (cpf.length !== 11) {
        alert("CPF deve conter 11 dígitos.");
        return;
    }

    try {
        const resposta = await fetch("http://localhost:5000/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                cpf: cpf,
                senha: senha
            })
        });

        const dados = await resposta.json();

        if (resposta.ok) {
        alert("Bem-vindo, " + dados.nome + "!");
        window.location.href = "../TelaAgendamentos/Agendamentos.html";
        } else {
                alert(dados.mensagem);
        }

    } catch (erro) {
        alert("Erro ao conectar com o servidor.");
        console.error(erro);
    }
});
