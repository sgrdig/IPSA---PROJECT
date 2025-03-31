import java.util.Date;

public class Emprunts {
    private int codeDocuments;
    private int codeA;
    private Date dateEmprunt;

    public Emprunts(int codeDocuments, Adherents adherent, Date dateEmprunt) {
        this.codeDocuments = codeDocuments;
        this.codeA = adherent.getCodeA();
        this.codeA = codeA;
        this.dateEmprunt = dateEmprunt;
    }

}