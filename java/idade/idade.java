package idade;

import java.util.Scanner;

public class idade {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int i;
        int c = 0;
        double soma = 0;

        System.out.println(" ");
        System.out.println(" ");
        System.out.println("calcular maiores de idade");
        System.out.println("-------------------------");
        System.out.println(" ");

        

        for (i = 1; i <= 10; i++) {
            System.out.println("usuario: " + i + " | digite a sua idade: ");
            double idade = scanner.nextInt();

            if (idade >= 18) {
                c += 1;
            }

            soma += idade;
        }

        System.out.println(" ");

        System.out.println("quantidade de maiores de 18 anos: " + c);
        System.out.println("soma de todas as idades: " + soma);
    }
}
