public class Exemplaire {
    private static int compteur = 0;
    private int numInv;
    private String nature;
    private float prix;
    private Boolean etatDispo;

    public Exemplaire(String nature, float prix, Boolean etatDispo) {
        this.numInv = ++compteur;
        this.nature = nature;
        this.prix = prix;
        this.etatDispo = etatDispo;
    }

    public int getNumInv() {
        return numInv;
    }

    public String getNature() {
        return nature;
    }

    public float getPrix() {
        return prix;
    }

    public Boolean getEtatDispo() {
        return etatDispo;
    }

    public void setNature(String nature) {
        this.nature = nature;
    }

    public void setPrix(float prix) {
        this.prix = prix;
    }

    public void setEtatDispo(Boolean etatDispo) {
        this.etatDispo = etatDispo;
    }

    @Override
    public String toString() {
        return "Exemplaire{" +
                "numInv=" + numInv +
                ", nature='" + nature + '\'' +
                ", prix=" + prix +
                ", etatDispo=" + etatDispo +
                '}';
    }
}
