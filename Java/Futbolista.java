import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

public class Futbolista {
    private String dni;
    private String nome;
    private int idade;
    private int numeroGoles;

    public Futbolista(String dni, String nome, int idade, int numeroGoles) {
        this.dni = dni;
        this.nome = nome;
        this.idade = idade;
        this.numeroGoles = numeroGoles;
    }

    public String getDni() {
        return dni;
    }

    public String getNome() {
        return nome;
    }

    public int getIdade() {
        return idade;
    }

    public int getNumeroGoles() {
        return numeroGoles;
    }

    public String toString() {
        return "Nome: " + nome + ", DNI: " + dni + ", Idade: " + idade + ", Número de goles: " + numeroGoles;
    }

    public boolean equals(Object o) {
        Futbolista f = (Futbolista) o;
        return dni.equals(f.dni);
    }

    public static Comparator<Futbolista> compararPorDni =
            new Comparator<Futbolista>() {
                public int compare(Futbolista f1, Futbolista f2) {
                    return f1.dni.compareTo(f2.dni);
                }
            };

    public static Comparator<Futbolista> compararPorNome =
            new Comparator<Futbolista>() {
                public int compare(Futbolista f1, Futbolista f2) {
                    return f1.nome.compareToIgnoreCase(f2.nome);
                }
            };

    public static Comparator<Futbolista> compararPorGoles =
            new Comparator<Futbolista>() {
                public int compare(Futbolista f1, Futbolista f2) {
                    return Integer.compare(f1.numeroGoles, f2.numeroGoles);
                }
            };

    public static void main(String[] args) {

        ArrayList<Futbolista> lista = new ArrayList<>();

        lista.add(new Futbolista("333A", "Pedro", 25, 10));
        lista.add(new Futbolista("111B", "Luis", 22, 15));
        lista.add(new Futbolista("222C", "Ana", 27, 7));

        System.out.println("LISTA ORIGINAL");
        for (Futbolista f : lista) {
            System.out.println(f);
        }

        Collections.sort(lista, Futbolista.compararPorDni);

        System.out.println("\nORDENADOS POR DNI");
        for (Futbolista f : lista) {
            System.out.println(f);
        }

        Collections.sort(lista, Futbolista.compararPorNome);

        System.out.println("\nORDENADOS POR NOME");
        for (Futbolista f : lista) {
            System.out.println(f);
        }

        Collections.sort(lista, Futbolista.compararPorGoles);

        System.out.println("\nORDENADOS POR GOLES");
        for (Futbolista f : lista) {
            System.out.println(f);
        }

        Futbolista f1 = new Futbolista("999X", "Mario", 20, 5);
        Futbolista f2 = new Futbolista("999X", "Carlos", 30, 12);
        System.out.println("\nPROBA EQUALS");
        System.out.println(f1.equals(f2));
    }
}