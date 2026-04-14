import java.sql.SQLOutput;

public class Hora {
    int horas;
    int minutos;
    int segundos;

    public Hora(){
        inicializaACero();
    }

    public Hora(int horas, int minutos, int segundos){
        if (horas >= 0) this.horas = horas;
        else this.horas = 0;
        if (minutos < 60 && minutos >= 0) this.minutos = minutos;
        else this.minutos = 0;
        if (segundos < 60 && segundos >= 0) this.segundos = segundos;
        else this.segundos = 0;
    }

    public Hora(String hora){
        if (hora.length() != 8){
            if (hora.charAt(2) == ':' && hora.charAt(5) == ':') {

            }
            else {
                System.out.println("Formato da hora incorrecta");
                inicializaACero();
            }
        else {
                System.out.println("Lonxitude da hora incorrecta");
                inicializaACero();
            }
        }
    }

    private inicializaACero(){
        horas = 0;
        minutos = 0;
        segundos = 0;
    }

    public String toString(){
        return "Hora: " + horas + ", Minutos: " + minutos + ", Segundos: " + segundos;
    }

    public static void main(String [] args){
        Hora h = new Hora();
        System.out.println(h);
    }
}
