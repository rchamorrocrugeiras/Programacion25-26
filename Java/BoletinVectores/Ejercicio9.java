package BoletinVectores;

public class Ejercicio9 {

    public static void ordenar(short[] arr) {
        for (int i = 0; i < arr.length - 1; i++) {
            for (int j = 0; j < arr.length - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    short temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    }

    public static boolean busquedaBinaria(short[] arr, int size, short valor) {
        int izquierda = 0;
        int derecha = size - 1;

        while (izquierda <= derecha) {
            int medio = (izquierda + derecha) / 2;

            if (arr[medio] == valor) {
                return true;
            } else if (arr[medio] < valor) {
                izquierda = medio + 1;
            } else {
                derecha = medio - 1;
            }
        }
        return false;
    }

    public static short[] eliminarRepetidos(short[] entrada) {

        ordenar(entrada);

        short[] resultado = new short[entrada.length];
        int size = 0;

        for (int i = 0; i < entrada.length; i++) {
            if (!busquedaBinaria(resultado, size, entrada[i])) {
                resultado[size] = entrada[i];
                size++;
            }
        }

        short[] salida = new short[size];

        for (int i = 0; i < size; i++) {
            salida[i] = resultado[i];
        }

        return salida;
    }

    public static void main(String[] args) {

        short[] datos = {5, 3, 8, 3, 5, 1};

        short[] sinRepetidos = eliminarRepetidos(datos);

        for (int i = 0; i < sinRepetidos.length; i++) {
            System.out.print(sinRepetidos[i] + " ");
        }
    }
}
