const form = document.getElementById("Form");
const nomeInput = document.getElementById("nome");
const cpfInput = document.getElementById("cpf");
const senhaInput = document.getElementById("senha");

form.addEventListener("submit", async function (event) {
    event.preventDefault();

    const nome = nomeInput.value.trim();
    const cpf = cpfInput.value.trim();
    const senha = senhaInput.value.trim();

    if (nome === "" || cpf === "" || senha === "") {
        alert("Preencha todos os campos.");
        return;
    }

    if (cpf.length !== 11) {
        alert("CPF deve conter 11 dígitos.");
        return;
    }

    try {
        const resposta = await fetch("http://localhost:5000/usuarios", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                nome: nome,
                cpf: cpf,
                senha: senha
            })
        });

        const dados = await resposta.json();

        if (resposta.ok) {
            alert(dados.mensagem);
            form.reset();
        } else {
            alert("Erro: " + dados.mensagem);
        }

    } catch (erro) {
        alert("Erro ao conectar com o servidor.");
        console.error(erro);
    }
});
