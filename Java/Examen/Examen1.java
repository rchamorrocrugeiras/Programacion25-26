import java.util.ArrayList;
import java.util.Comparator;
import java.util.Scanner;

// 1. Clase Contacto
public class Contacto {
    private final String nome;
    private String numtelefono;
    private String empresa;

    public Contacto(String nome, String numTelefono, String empresa) {
        this.nome = nome;
        this.numtelefono = numTelefono;
        this.empresa = empresa;
    }

    public String getNome() {
        return this.nome;
    }

    public String getNumeroTelefono() {
        return this.numtelefono;
    }

    public void setNumeroTelefono(String numTelef) {
        this.numtelefono = numTelef;
    }

    public String getEmpresa() {
        return this.empresa;
    }

    public void setEmpresa(String empresa) {
        this.empresa = empresa;
    }

    public boolean equals(Object outro) {
        Contacto c = (Contacto) outro;
        return nome.equals(c.nome) && numtelefono.equals(c.numtelefono) && empresa.equals(c.empresa);
    }

    public String toString() {
        return "Nome: " + nome + ", Teléfono: " + numtelefono + ", Empresa: " + empresa;
    }
}

// 2. Clase Comparador Contactos
class ComparadorContactos implements Comparator<Contacto> {
    public int compare(Contacto c1, Contacto c2) {
        int resto = c1.getNome().compareTo(c2.getNome());
        if (resto == 0) {
            return c1.getNumeroTelefono().compareTo(c2.getNumeroTelefono());
        }
        return resto;
    }
}

// 3. Clase Listin Telefonico
class ListinTelefonico {
    private final String nome;
    private ArrayList<Contacto> contactos;

    public ListinTelefonico(String nome) {
        this.nome = nome;
        this.contactos = new ArrayList<>();
    }

    public String get_nome() {
        return this.nome;
    }

    public Contacto getContacto(String nome) {
        for (Contacto c : contactos) {
            if (c.getNome().equals(nome)) return c;
        }
        return null;
    }

    public boolean addContacto(Contacto c) {
        for (Contacto aux : contactos) {
            if (aux.equals(c)) return false;
        }
        contactos.add(c);
        return true;
    }

    public ArrayList<Contacto> getContactosEmpresa(String empresa) {
        ArrayList<Contacto> lista = new ArrayList<>();
        for (Contacto c : contactos) {
            if (c.getEmpresa().equals(empresa)) {
                lista.add(c);
            }
        }
        return lista;
    }

    public boolean borrarContacto(Contacto c) {
        return contactos.remove(c);
    }

    public void mostrarListaContactos(String empresa) {
        for (Contacto c : contactos) {
            if (c.getEmpresa().equals(empresa)) System.out.println(c);
        }
    }
}

// 4. Programa principal
public class Principal {
    public static void main(String[] args) {
        System.out.println("a) Engadir contacto");
        System.out.println("b) Eliminar contacto");
        System.out.println("c) Mudar o telefono dun contacto");
        System.out.println("d) Mostrar a lista de contactos dunha empresa");
        System.out.println("e) Sair");
    }
}

// 5. Clase Telefono
public class Telefono {
    public boolean verificarFormatoTelefono(String telefono){
        if (telefono.length() != 15) {
            return false;
        }
        if (telefono.charAt(0) != '+') {
            return false;
        }
        if (telefono.charAt(3) != " " && telefono.charAt(7) != " " && telefono.charAt(11) != " ") {
            return false;
        }
        for (int i = 1; i < telefono.length(); i++) {
            if (i == 3 || i == 7 || i == 11) {
                continue;
            }
            if (telefono.charAt(i) < 0 || telefono.charAt(i) > 9) {
                return false;
            }
        }
        return true;
    }
}