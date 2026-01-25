const form = document.getElementById("form")

form.addEventListener("submit", function (event){
    event.preventDefault();

    const nome = document.getElementById("nome").value;
    const email = document.getElementById("email").value;

    fetch("http://127.0.0.1:5000/Logar", {
        method: "POST",
        headers: {
             "Content-Type": "application/json"
        },
        body: JSON.stringify({
            nome: nome,
            email: email
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
        alert("Usuário logado com sucesso!");
        console.log(data);
    
    })
    .catch(error => {
        alert(error.erro || "Nome ou email incorreto");
        console.error(error);
    });
});




