import java.util.ArrayList;
import java.util.List;

public class Document {
    float code;
    String discipline;
    String theme;
    int dateEdition;
    String langue;
    int nbrExpl;
    int nbrExplDispo = 1;
    static List<Document> documents = new ArrayList<>(); 

    public Document(float code, int dateEdition, String discipline, String langue, int nbrExpl, int nbrExplDispo, String theme) {
        this.code = code;
        this.dateEdition = dateEdition;
        this.discipline = discipline;
        this.langue = langue;
        this.nbrExpl = nbrExpl;
        this.theme = theme;
        for (Document doc : documents) {
            if (doc.code == code) {
                doc.nbrExpl += 1;
                doc.nbrExplDispo += 1;
                return;
            }
        }

        documents.add(this);
    }

    @Override
    public String toString() {
        return "Document{" +
                "code=" + code +
                ", discipline='" + discipline + '\'' +
                ", theme='" + theme + '\'' +
                ", dateEdition=" + dateEdition +
                ", langue='" + langue + '\'' +
                ", nbrExpl=" + nbrExpl +
                ", nbrExplDispo=" + nbrExplDispo +
                '}';
    }

    public void allDocs() {
        for (Document doc : documents) {
            System.out.println(doc.toString());
        }
    }

    public void empruntDocs(float code, Adherents adherent, java.util.Date dEmprunt) {
        for (Document doc : documents) {
            if (doc.code == code && doc.nbrExplDispo > 0) {
                doc.nbrExplDispo -= 1;

                Emprunts e = new Emprunts((int) code, adherent, dEmprunt);
                System.out.println("Doc emprunté avc succès: " + e);
                return;
            }
        }
        System.out.println("Pas de Docs dispo, réessaye pls");
    }

    public void miseaJour(float code, int dateEdition, String discipline, String langue, int nbrExpl, int nbrExplDispo, String theme) {
        for (Document doc : documents) {
            if (doc.code == code) {
                doc.dateEdition = dateEdition;
                doc.discipline = discipline;
                doc.langue = langue;
                doc.nbrExpl = nbrExpl;
                doc.nbrExplDispo = nbrExplDispo;
                doc.theme = theme;
                System.out.println("Doc avc code " + code + " maj.");
                return;
            }
        }
        System.out.println("Aucun doc trouvé avc code " + code + ".");
    }

    public void recherche(float code) {
        int cpt = 0;
        for (Document document : documents) {
            if (document.code == code) {
                cpt += 1;
                System.out.println(document.toString());
            }
        }
        System.out.println("Y'a " + cpt + " doc(s) ki correspond(ent) à ta demande.");
    }

    public static void main(String[] args) {

        Document doc1 = new Document(1.0f, 2023, "Maths", "Anglais", 10, 8, "Algèbre");
        Document doc2 = new Document(2.0f, 2022, "Physique", "Français", 5, 3, "Mécanique");

        System.out.println("Tous les Docs:");
        doc1.allDocs();

        System.out.println("\nMaj du Doc avc code 1.0:");
        doc1.miseaJour(1.0f, 2024, "Maths", "Anglais", 15, 12, "Algèbre Avancée");
        doc1.allDocs();

        System.out.println("\nRecherche du Doc avc code 2.0:");
        doc1.recherche(2.0f);

        System.out.println("\nEmprunt du Doc avc code 1.0:");
        Adherents adherent = new Adherents("123 Rue", 1, "email@example.com", "Jean", "Dupont", Privilege.ETUDIANT, "123456789");
        doc1.empruntDocs(1.0f, adherent, new java.util.Date());
        doc1.allDocs();

        System.out.println("\nEmprunt du Doc avc code 1.0 encore:");
        doc1.empruntDocs(1.0f, adherent, new java.util.Date());
    }
}
