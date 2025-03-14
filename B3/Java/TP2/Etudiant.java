
import java.util.Arrays;

class Etudiant {
    private String nom;
    private String prenom;
    private int numero;
    static int nbrtucree = 0 ;
    int notes[];
    String coursuivis[];


    public Etudiant(String nom, String[] coursuivis, String prenom) {
        this.nom = nom;
        this.prenom = prenom;
        nbrtucree += 1;
        numero = nbrtucree;
        notes = new int[coursuivis.length];
        for (int i = 0; i < notes.length; i++) {
            notes[i] = 0;
        }
        Arrays.fill(notes, 0);
    }

    @Override public String toString() {
        return "Nom: " + nom + ", Prenom: " + prenom + ", Numero: " + numero + ", Cours suivis: " + Arrays.toString(coursuivis) + ", Notes: " + Arrays.toString(notes);
    }


    public static void main(String[] args) {
        Etudiant e1 =  new Etudiant("bob", new String[]{"maths", "francais"}, "billy");
        Etudiant e2 = new Etudiant("Thomas", new String[]{"math , it , aero"}, "George");
        System.out.println(e1.numero);
        System.out.println(e2.numero);
        e1.toString();
        System.out.println(e1);

    }
}