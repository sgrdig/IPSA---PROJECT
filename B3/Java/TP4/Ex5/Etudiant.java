import java.util.List;

public class Etudiant {
    private String cne;
    private String cin;
    private String nom;
    private String prenom;
    private String dateNaissance;
    private String villeNaissance;
    private String adresse;
    private String email;
    private int niveau;
    private List<Double> notesParSemestre;

    public Etudiant(String cne, String cin, String nom, String prenom, String dateNaissance, 
                    String villeNaissance, String adresse, String email, int niveau, 
                    List<Double> notesParSemestre) {
        this.cne = cne;
        this.cin = cin;
        this.nom = nom;
        this.prenom = prenom;
        this.dateNaissance = dateNaissance;
        this.villeNaissance = villeNaissance;
        this.adresse = adresse;
        this.email = email;
        this.niveau = niveau;
        this.notesParSemestre = notesParSemestre;
    }

    public String getCne() {
        return cne;
    }

    public void setCne(String cne) {
        this.cne = cne;
    }

    public String getCin() {
        return cin;
    }

    public void setCin(String cin) {
        this.cin = cin;
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

    public String getDateNaissance() {
        return dateNaissance;
    }

    public void setDateNaissance(String dateNaissance) {
        this.dateNaissance = dateNaissance;
    }

    public String getVilleNaissance() {
        return villeNaissance;
    }

    public void setVilleNaissance(String villeNaissance) {
        this.villeNaissance = villeNaissance;
    }

    public String getAdresse() {
        return adresse;
    }

    public void setAdresse(String adresse) {
        this.adresse = adresse;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public int getNiveau() {
        return niveau;
    }

    public void setNiveau(int niveau) {
        this.niveau = niveau;
    }

    public List<Double> getNotesParSemestre() {
        return notesParSemestre;
    }

    public void setNotesParSemestre(List<Double> notesParSemestre) {
        this.notesParSemestre = notesParSemestre;
    }

    @Override
    public String toString() {
        return "Etudiant{" +
                "cne='" + cne + '\'' +
                ", cin='" + cin + '\'' +
                ", nom='" + nom + '\'' +
                ", prenom='" + prenom + '\'' +
                ", niveau=" + niveau +
                '}';
    }
}
