public class Adherents {
    public int codeA;
    public String prenom;
    public String nom;
    public String tel;
    public String adresse;
    public String email;
    public Privilege privilege;

    public Adherents(String adresse, int codeA, String email, String nom, String prenom, Privilege privilege, String tel) {
        this.adresse = adresse;
        this.codeA = codeA;
        this.email = email;
        this.nom = nom;
        this.prenom = prenom;
        this.privilege = privilege;
        this.tel = tel;
    }

    public int getCodeA() {
        return codeA;
    }
}