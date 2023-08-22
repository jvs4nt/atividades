package votos;

import java.util.Scanner;

public class votos {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int[] votos = new int[5]; // Índices 1 a 4 representam os candidatos; índice 0 = nulo; índice 5 = branco

        int voto;
        do {
            System.out.print("Digite o código do candidato (1 a 4), 5 para voto nulo, 6 para voto em branco, ou 0 para encerrar: ");
            voto = scanner.nextInt();

            switch (voto) {
                case 1:
                case 2:
                case 3:
                case 4:
                    votos[voto]++;
                    break;
                case 5:
                    votos[0]++; // Voto nulo
                    break;
                case 6:
                    votos[5]++; // Voto em branco
                    break;
                case 0:
                    break; // Encerrar a votação
                default:
                    System.out.println("Código inválido. Digite novamente.");
            }
        } while (voto != 0);

        System.out.println("Total de votos para cada candidato:");
        for (int i = 1; i <= 4; i++) {
            System.out.println("Candidato " + i + ": " + votos[i]);
        }
        System.out.println("Total de votos nulos: " + votos[0]);
        System.out.println("Total de votos em branco: " + votos[5]);

        scanner.close();
    }
}