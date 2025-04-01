import java.util.List;


public class Rapport extends Document {
    private String auteur;

    public Rapport(float code, int dateEdition, String discipline, String langue, int nbrExpl, int nbrExplDispo, String theme ,List<Document> documents) {
        super(code, dateEdition, discipline, langue, nbrExpl, nbrExplDispo, theme , documents);
        this.auteur = auteur;
    }


    public String getAuteur() {
        return auteur;
    }

    public void setAuteur(String auteur) {
        this.auteur = auteur;
    }
}