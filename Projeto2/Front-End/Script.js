const form = document.getElementById("form");
const mensagem = document.getElementById("mensagem");

form.addEventListener("submit", function (event) {
    event.preventDefault();

    const cep = document.getElementById("CEP").value;

    // limpa mensagem anterior
    mensagem.textContent = "";
    mensagem.className = "";

    fetch("http://127.0.0.1:5000/cep", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ cep: cep })
    })
    .then(response => {
        return response.json().then(data => {
            if (!response.ok) {
                throw data;
            }
            return data;
        });
    })
    .then(data => {
        mensagem.textContent = `✅ CEP encontrado: ${data.cidade} - ${data.estado}`;
        mensagem.classList.add("sucesso");
    })
    .catch(error => {
        mensagem.textContent = "❌ CEP não encontrado no banco";
        mensagem.classList.add("erro");
        console.error(error);
    });
});
