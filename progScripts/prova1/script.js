$(document).ready(function() {
    $("#botao").click(function() {
        var n = parseInt($("#numero").val());
        
        if (!isNaN(n)) {
            var calculo = fatorial(n);
            $("#resultado").text(`o fatorial de ${n} é ${calculo}.`);
            $("#slidedown").slideDown();
        } else {
            alert("digite um valor");
        }
    });
});

function fatorial(n) {
    if (n === 0 || n === 1) {
        return 1;
    } else {
        return n * fatorial(n - 1);
    }
}
