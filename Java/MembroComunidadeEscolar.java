public class MembroComunidadeEscolar extends Persoa{
    private int codigoCentro;
    private String nomeCentro;

    public MembroComunidadeEscolar(String nome, String dni, int edade, int codCentro, String nomCentro) {
        super(nome, dni, edade);
        this.codigoCentro = codCentro;
        this.nomeCentro = nomCentro;
    }

    public String getCodigoCentro() {
        return this.codigoCentro;
    }

    public void setCodigoCentro(int novoCodCentro) {
        if (novoCodCentro > 0) codigoCentro = novoCodCentro;
        else codigoCentro = 0;
    }

    public String getNomeCentro() {
        return nomeCentro;
    }

    public void setNomeCentro(String nomeCentro) {
        this.nomeCentro = nomeCentro;
}