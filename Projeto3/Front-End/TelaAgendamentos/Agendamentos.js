const checkboxes = document.querySelectorAll(".servico");
const valorTotal = document.getElementById("valorTotal");
const form = document.getElementById("formAgendamento");

checkboxes.forEach(function(checkbox) {
    checkbox.addEventListener("change", calcularTotal);
});

function calcularTotal() {
    let total = 0;

    checkboxes.forEach(function(checkbox) {
        if (checkbox.checked) {
            total += parseFloat(checkbox.value);
        }
    });

    valorTotal.textContent = "R$ " + total;
}

form.addEventListener("submit", function(event) {
    event.preventDefault();

    const data = document.getElementById("data").value;
    const hora = document.getElementById("hora").value;

    if (valorTotal.textContent === "R$ 0" || data === "" || hora === "") {
        alert("Selecione ao menos um serviço e preencha data e hora.");
        return;
    }

    alert("Agendamento realizado! Total: " + valorTotal.textContent);
});

