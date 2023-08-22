package positivos;

import java.util.Scanner;

public class positivos {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int quantidadeValores = 0;
        int somatorio = 0;
        int valor;

        do {
            System.out.print("Digite um valor positivo (ou 0/negativo para encerrar): ");
            valor = scanner.nextInt();

            if (valor > 0) {
                somatorio += valor;
                quantidadeValores++;
            } else if (valor < 0) {
                System.out.println("Valor negativo digitado. Encerrando...");
            }
        } while (valor > 0);

        if (quantidadeValores > 0) {
            double media = (double) somatorio / quantidadeValores;
            System.out.println("Somatório dos valores positivos: " + somatorio);
            System.out.println("Média dos valores positivos: " + media);
        } else {
            System.out.println("Nenhum valor positivo digitado.");
        }

        scanner.close();
    }
}