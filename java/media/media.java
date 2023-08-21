package media;

import java.util.Scanner;

public class media {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println(" ");
        System.out.println(" ");
        System.out.println("calcular media entre duas notas");
        System.out.println("-------------------------------");
        System.out.println(" ");

        System.out.println("digite o valor da sua primeira nota: ");
        double n1 = scanner.nextDouble();

        System.out.println(" ");

        System.out.println("digite o valor da sua segunda nota: ");
        double n2 = scanner.nextDouble();

        System.out.println(" ");

        double media = (n1 + n2) / 2;

        if (media >= 0 && media < 4) {
            System.out.println("voce foi reprovado com media: " + media);
        }
        else if (media >= 4 && media < 7) {
            System.out.println("voce esta de exame com media: " + media);
        }
        else if (media >= 7 && media <= 10) {
            System.out.println("voce foi aprovado com media: " + media);
        }
        else {
            System.out.println("digite valores validos");
        }
    }
}
