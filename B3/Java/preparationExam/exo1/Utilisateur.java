import java.util.List;

public class Utilisateur {
    private String nom;
    private String prenom;
    private String email;
    private List<Billet> billetsReserve;

    public Utilisateur(String nom, String prenom, String email, List<Billet> billetsReserve) {
        this.nom = nom;
        this.prenom = prenom;
        this.email = email;
        this.billetsReserve = billetsReserve;
    }

    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public String getPrenom() {
        return prenom;
    }

    public void setPrenom(String prenom) {
        this.prenom = prenom;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public List<Billet> getBilletsReserve() {
        return billetsReserve;
    }

    public void setBilletsReserve(List<Billet> billetsReserve) {
        this.billetsReserve = billetsReserve;
    }
}
