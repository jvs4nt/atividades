package turma;

import java.util.Scanner;

public class turma {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int quantidadeAlunos = 10;
        int aprovados = 0;
        int reprovados = 0;
        double somaMedias = 0;
        double maiorMedia = Double.MIN_VALUE;
        double menorMedia = Double.MAX_VALUE;

        for (int i = 1; i <= quantidadeAlunos; i++) {
            System.out.println("Aluno " + i);
            System.out.print("Número de matrícula: ");
            int matricula = scanner.nextInt();

            System.out.print("Digite as 3 notas: ");
            double nota1 = scanner.nextDouble();
            double nota2 = scanner.nextDouble();
            double nota3 = scanner.nextDouble();

            System.out.print("Frequência (número de aulas frequentadas): ");
            int frequencia = scanner.nextInt();

            double media = (nota1 + nota2 + nota3) / 3;
            somaMedias += media;

            if (media >= 6.0 && ((double) frequencia / 75) >= 1.0) {
                System.out.println("Código: Aprovado");
                aprovados++;
            } else {
                System.out.println("Código: Reprovado");
                reprovados++;
            }

            if (media > maiorMedia) {
                maiorMedia = media;
            }
            if (media < menorMedia) {
                menorMedia = media;
            }

            System.out.println("Número de matrícula: " + matricula);
            System.out.println("Frequência: " + frequencia + " aulas");
            System.out.println("Nota final: " + media);
        }

        double mediaGeral = somaMedias / quantidadeAlunos;

        System.out.println("\nMaior média da turma: " + maiorMedia);
        System.out.println("Menor média da turma: " + menorMedia);
        System.out.println("Média geral da turma: " + mediaGeral);
        System.out.println("Número de alunos aprovados: " + aprovados);
        System.out.println("Número de alunos reprovados: " + reprovados);

        scanner.close();
    }
}