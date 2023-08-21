$(document).ready(function() {
    $("#calcular").click(function() {
        var largura = parseFloat($("#largura").val());
        var altura = parseFloat($("#altura").val());

        if (isNaN(largura) || isNaN(altura) || largura <= 0 || altura <= 0) {
            alert("Digite as dimensões");
            return;
        }

        var area = largura * altura;
        var figura = largura === altura ? "quadrado" : "retangulo";

        var resultText = `a area da figura é: ${area}<br>nome da figura: ${figura}`;
        var figura = "quadrado";

        $("#resultadoToast").html(resultText);

        var toast = new bootstrap.Toast($("#exibirToast")[0]);
        toast.show();
    });
});
