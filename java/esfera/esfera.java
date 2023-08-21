package esfera;
import java.util.Scanner;

class esfera {
    public static void main(String[] args) {

        double c;
        double pi = Math.PI;
        double raio;
        double area;
        double exponente = 2;
        double exponente3 = 3;
        double raioElevado;
        double volume;
        double raioElevadoTres;

        Scanner scanner = new Scanner(System.in);

        System.out.println("digite o raio da esfera:");
        raio = scanner.nextInt();

        c = 2 * pi * raio;
        
        raioElevado = Math.pow(raio, exponente);
        raioElevadoTres = Math.pow(raio, exponente3);

        area = pi * raioElevado;

        volume = (3.0 / 4) * pi * raioElevadoTres;

        String formatC = String.format("%.2f", c);

        System.out.println("raio = " + raio);
        System.out.println("pi = " + pi);
        System.out.println("o comprimento da esfera é: " + formatC);
        System.out.println("a area da esfera é: " + area);
        System.out.println("o volume da esfera é: " + volume);

        scanner.close();
    }
}
