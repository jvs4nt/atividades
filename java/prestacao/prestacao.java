package prestacao;

import java.util.Scanner;

public class prestacao {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println(" ");
        System.out.println(" ");
        System.out.println("calcular prestacao");
        System.out.println("----------------------");
        System.out.println(" ");

        System.out.println("digite o valor da prestacao: ");
        double valor = scanner.nextDouble();

        System.out.println("digite o valor da taxa de juros (em %): ");
        double taxa = scanner.nextDouble();

        System.out.println("digite a quantidade de meses em atraso: ");
        int meses = scanner.nextInt();

        double prestacao = valor + (valor * (taxa / 100) * meses);

        System.out.println("o valor das prestacoes em atraso sera: " + prestacao);


    }
}
