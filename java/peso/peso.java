package peso;

import java.util.Scanner;

public class peso {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        double pesoIdeal;

        System.out.println(" ");
        System.out.println(" ");
        System.out.println("calcular peso ideal");
        System.out.println("--------------------");
        System.out.println(" ");

        System.out.println("digite a sua altura (ex. 1.75): ");
        double altura = scanner.nextDouble();

        System.out.println(" ");

        System.out.println("digite seu sexo: ");
        System.out.println("(1 - FEMININO / 2 - MASCULINO)");
        int sexo = scanner.nextInt();

        switch (sexo) {
            case 1:
            pesoIdeal = (62.1 * altura) - 44.7;
            System.out.println("peso ideal: " + pesoIdeal);
            break;

            case 2:
            pesoIdeal = (72.7 * altura) - 58;
            System.out.println("peso ideal: " + pesoIdeal);
            break;
            
        }
    }
}
