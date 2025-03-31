public class Rapport extends Document {
    private String auteur;

    public Rapport(float code, int dateEdition, String discipline, String langue, int nbrExpl, int nbrExplDispo, String theme, String auteur) {
        super(code, dateEdition, discipline, langue, nbrExpl, nbrExplDispo, theme);
        this.auteur = auteur;
    }

    public String getAuteur() {
        return auteur;
    }

    public void setAuteur(String auteur) {
        this.auteur = auteur;
    }
}