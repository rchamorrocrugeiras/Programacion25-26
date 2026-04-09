public class MembroComunidadeEscolar extends Persoa{
    private int codigoCentro;
    private String nomeCentro;

    public MembroComunidadeEscolar(String nome, String dni, int edade, int codCentro, String nomCentro) {
        super(nome, dni, edade);
        this.codigoCentro = codCentro;
        this.nomeCentro = nomCentro;
    }
}
