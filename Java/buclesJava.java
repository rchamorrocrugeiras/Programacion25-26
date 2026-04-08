import java.util.Scanner;

public class buclesJava {
    public static void main (String[] args){
        //Bucle while
        int contador = 0;
        while (contador <= 5) {
            System.out.println("Bucle while " + contador);
            contador++;
        }
        //Buvle do-while
        contador = 0;
        do {
            System.out.println("Bucle do-while " + contador);
            contador++;
        } while (contador <= 5);
        //Scanner es como un input en python
        Scanner teclado = new Scanner(System.in);
        int opcion = 0;
        while (opcion != 3) {
            System.out.println("Elixe unha opción");
            System.out.println("1.Saudar");
            System.out.println("2.Despedirse");
            System.out.println("3.Sair");
            String op = teclado.nextLine();
            opcion = Integer.parseInt(op);
            switch (opcion) {
                case 1:
                    System.out.println("Bienvenido");
                    break;
                case 2:
                    System.out.println("Hasta luego");
                    break;
                case 3:
                    System.out.println("Programa cerrado");
                    break;
                default:
                    System.out.println("Error de opcion");
                    break;
            }
        }
        for (int i = 5; i < 20 ;i += 3) {
            System.out.println("Indice: " + i);
        }
        int i = 5;
        for(;;){
            System.out.println("Indice: "+ i);
            i += 3;
            if (i > 19) break;
        }
    }
}
