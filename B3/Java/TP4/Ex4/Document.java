import java.util.List;

public class Document {

    float code;
    String discipline;
    String theme;
    int dateEdition;
    String langue;
    int nbrExpl;
    int nbrExplDispo = 1;
    //static List<Document> documents = new ArrayList<>(); 

    public Document(float code, int dateEdition, String discipline, String langue, int nbrExpl, int nbrExplDispo, String theme ,List<Document> documents ) {
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

        //documents.add(this);
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

    public void allDocs(List<Document> documents ) {
        for (Document doc : documents) {
            System.out.println(doc.toString());
        }
    }

    public void empruntDocs(float code, Adherents adherent, java.util.Date dEmprunt , List<Document> documents ) {
        for (Document doc : documents) {
            if (doc.code == code && doc.nbrExplDispo > 0) {
                doc.nbrExplDispo -= 1;

                Emprunts e = new Emprunts((int) code, adherent, dEmprunt);
                System.out.println("Doc emprunte avc succes: " + e);
                return;
            }
        }
        System.out.println("Pas de Docs dispo, réessaye pls");
    }

    public void miseaJour(float code, int dateEdition, String discipline, String langue, int nbrExpl, int nbrExplDispo, String theme , List<Document> documents ) {
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
        System.out.println("Aucun doc trouve avc code " + code + ".");
    }

    public void recherche(float code , List<Document> documents ) {
        int cpt = 0;
        for (Document document : documents) {
            System.err.println("code: " + document.code + " recherche: " + code);
            if (document.code == code) {
                cpt += 1;
                System.out.println(document.toString());
            }
        }
        System.out.println("Y'a " + cpt + " doc ou docs ki corresponde (ent)");
    }

    


    /*public static void main(String[] args) {

        Document doc1 = new Document(1, 2023, "Maths", "Anglais", 10, 8, "Algebre");
        Document doc2 = new Document(2, 2022, "Physique", "Francais", 5, 3, "Mecanique");

        Document doc3 = new Document(1, 2023, "Maths", "Francais", 10, 8, "Algebre");


        System.out.println("Tous les Docs:");
        doc1.allDocs();

        System.out.println("\nMaj du Doc avc code 1.0:");
        doc1.miseaJour(1.0f, 2024, "Maths", "Anglais", 15, 12, "Algebre ++");
        doc1.allDocs();

        System.out.println("\nRecherche du Doc avc code 2.0:");
        doc1.recherche(1);

        System.out.println("\nRecherche du Doc avc code 2.0:");
        doc1.recherche(2);

        System.out.println("\nEmprunt du Doc avc code 1.0:");
        Adherents adherent = new Adherents("123 Rue", 1, "tagrandmere@example.com", "Jean", "Dupont", Privilege.ETUDIANT, "123456789");
        doc1.empruntDocs(1.0f, adherent, new java.util.Date());
        doc1.allDocs();

        System.out.println("\nEmprunt du Doc avc code 1.0 encore:");
        doc1.empruntDocs(1.0f, adherent, new java.util.Date());
    }*/

    public float getCode() {
        return code;
    }

    public String getDiscipline() {
        return discipline;
    }

    public String getTheme() {
        return theme;
    }

    public int getDateEdition() {
        return dateEdition;
    }

    public String getLangue() {
        return langue;
    }

    public int getNbrExpl() {
        return nbrExpl;
    }

    public int getNbrExplDispo() {
        return nbrExplDispo;
    }

    public void setCode(float code) {
        this.code = code;
    }

    public void setDiscipline(String discipline) {
        this.discipline = discipline;
    }

    public void setTheme(String theme) {
        this.theme = theme;
    }

    public void setDateEdition(int dateEdition) {
        this.dateEdition = dateEdition;
    }

    public void setLangue(String langue) {
        this.langue = langue;
    }

    public void setNbrExpl(int nbrExpl) {
        this.nbrExpl = nbrExpl;
    }

    public void setNbrExplDispo(int nbrExplDispo) {
        this.nbrExplDispo = nbrExplDispo;
    }
}
