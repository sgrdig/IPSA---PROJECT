public class Privilege {

    public String nom;
    public int nbrDoc;
    public int nbrMaxEmprunts;

    public Privilege(int nbrDoc, int nbrMaxEmprunts, String nom) {
        this.nbrDoc = nbrDoc;
        this.nbrMaxEmprunts = nbrMaxEmprunts;
        this.nom = nom;
    }

    public static final Privilege ETUDIANT = new Privilege(5, 15, "Etudiant");
    public static final Privilege PROF = new Privilege(10, 30, "Prof");
    public static final Privilege ADMINISTRATEUR = new Privilege(15, 60, "Administrateur");

    @Override
    public String toString() {
        return "Privilege{" +
                "nom='" + nom + '\'' +
                ", nbrDoc=" + nbrDoc +
                ", nbrMaxEmprunts=" + nbrMaxEmprunts +
                '}';
    }
}