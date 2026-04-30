import org.w3c.dom.ls.LSOutput;
import java.sql.SQLOutput;

public class ejemplosArray {

    public static void main(String[] args) {

        int[] numeros = {1, 2, 3, 4, 5};
        char[] letras = new char[10];

        letras[0] = 'a';
        letras[1] = 'b';

        for (int i = 0; i < 5; i++)
            System.out.println("O número é: " + numeros[i]);

        for (int i = 0; i < letras.length; i++)
            System.out.println("A letra é: " + letras[i]);

        for (int n : numeros)
            System.out.println("O número é: " + n);

        String[] nomes = new String[10];

        nomes[0] = "Hugo";
        nomes[1] = "Pedro";
        nomes[2] = new String("Ana");

        Persoa[] equipo = new Persoa[5];

        equipo[0] = new Persoa("Ramón", "4567U", 41);
        equipo[1] = new Persoa("Jose", "8642H", 32);
        equipo[2] = new Persoa("Carmen", "9876Y", 41);
        equipo[3] = new Persoa("Fina", "1234R", 17);
        equipo[4] = new Persoa("Pili", "3258T", 33);

        // Contar o número total das letras dos nomes
        for (Persoa p : equipo) {
            int numLetras = 0;

            for (int i = 0; i < p.nome.length(); i++) {
                numLetras++;
            }

            System.out.println("As letras contadas de " + p.nome + " son: " + numLetras);
            System.out.println("As letras de " + p.nome + " son: " + p.nome.length());
        }

        // Encontrar o DNI lexicograficamente menor
        Persoa dniMenor = equipo[0];

        for (int i = 1; i < equipo.length; i++) {
            if (dniMenor.dni.compareTo(equipo[i].dni) > 0) {
                dniMenor = equipo[i];
            }
        }

        System.out.println("O dni " + dniMenor.dni + " de " + dniMenor.nome + " é lexicograficamente menor");
    }
}