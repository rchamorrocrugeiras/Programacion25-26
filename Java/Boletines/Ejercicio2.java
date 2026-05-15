package Boletines;

import java.util.ArrayList;
import java.util.Random;

public class Ejercicio2 {
    public static void main(String[] args){
        ArrayList<Integer> lista = new ArrayList<>();
        Random random = new Random();

        for (int i = 0; i < 100; i++){
            lista.add(random.nextInt(10) + 1);
        }

        System.out.println("Antes de eliminar:");
        System.out.println(lista);

        lista.removeIf(n -> n == 5 || n == 7);

        System.out.println("\nDespois de eliminar:");
        System.out.println(lista);
    }
}