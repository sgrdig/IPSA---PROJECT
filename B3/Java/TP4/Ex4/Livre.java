import java.util.List;

public class Livre extends Document {
    private String maisonEdi;
    private String codeISBN;
    private String auteurs;

    public Livre(float code, int dateEdition, String discipline, String langue, int nbrExpl, int nbrExplDispo, String theme ,List<Document> documents) {
        super(code, dateEdition, discipline, langue, nbrExpl, nbrExplDispo, theme , documents);
    
        this.codeISBN = codeISBN;
        this.maisonEdi = maisonEdi;
        this.auteurs = auteurs;
    }

    // Getters and setters
    public String getMaisonEdi() {
        return maisonEdi;
    }

    public void setMaisonEdi(String maisonEdi) {
        this.maisonEdi = maisonEdi;
    }

    public String getCodeISBN() {
        return codeISBN;
    }

    public void setCodeISBN(String codeISBN) {
        this.codeISBN = codeISBN;
    }

    public String getAuteurs() {
        return auteurs;
    }

    public void setAuteurs(String auteurs) {
        this.auteurs = auteurs;
    }
}