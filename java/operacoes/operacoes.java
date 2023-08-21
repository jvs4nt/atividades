package operacoes;

import java.util.Scanner;

public class operacoes {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
         
        System.out.println(" ");
        System.out.println(" ");
        System.out.println("executar operacoes");
        System.out.println("-------------------");

        System.out.println(" ");

        System.out.println("digite o primeiro valor: ");
        double n1 = scanner.nextDouble();

        System.out.println(" ");

        System.out.println("digite o segundo valor: ");
        double n2 = scanner.nextDouble();

        System.out.println(" ");

        System.out.println("escolha uma das opcoes:");
        System.out.println("1 - MEDIA ENTRE OS NUMEROS");
        System.out.println("2 - DIFERENCA DO MAIOR PARA O MENOR");
        System.out.println("3 - PRODUTO ENTRE OS NUMEROS");
        int i = scanner.nextInt();

        System.out.println(" ------------------- ");
        
        
        switch (i) {
            case 1:
                double media = (n1 + n2) / 2;
                System.out.println("media entre os numeros: " + media);
                break;
            case 2:
                if (n1 > n2) {
                    double resultado = n1 - n2;
                    System.out.println("diferenca do maior para o menor: " + resultado);
                    break;
                }
                else {
                    double resultado = n2 - n1;
                    System.out.println("diferenca do maior para o menor: " + resultado);
                    break;
                }
            case 3:
                double produto = n1 * n2;
                System.out.println("produto entre os numeros: " + produto);
                break;
        }
    }
}
