import java.util.ArrayList;
import java.util.List;
    
public class Biblio {

    static List<Document> documents = new ArrayList<>();

    static class Document {
        private String code;
        private String discipline;
        private String theme;
        private String type;
        private String dateEdition;
        private String langue;
        private int nombreExemplaires;
        private int nombreExemplairesDisponibles;

        public Document(String code, String discipline, String theme, String type, String dateEdition, String langue, int nombreExemplaires, int nombreExemplairesDisponibles) {
            this.code = code;
            this.discipline = discipline;
            this.theme = theme;
            this.type = type;
            this.dateEdition = dateEdition;
            this.langue = langue;
            this.nombreExemplaires = nombreExemplaires;
            this.nombreExemplairesDisponibles = nombreExemplairesDisponibles;
        }

        public String getCode() {
            return code;
        }

        public String getDiscipline() {
            return discipline;
        }

        public String getTheme() {
            return theme;
        }

        public String getType() {
            return type;
        }

        public String getDateEdition() {
            return dateEdition;
        }

        public String getLangue() {
            return langue;
        }

        public int getNombreExemplaires() {
            return nombreExemplaires;
        }

        public int getNombreExemplairesDisponibles() {
            return nombreExemplairesDisponibles;
        }

        public void setCode(String code) {
            this.code = code;
        }

        public void setDiscipline(String discipline) {
            this.discipline = discipline;
        }

        public void setTheme(String theme) {
            this.theme = theme;
        }

        public void setType(String type) {
            this.type = type;
        }

        public void setDateEdition(String dateEdition) {
            this.dateEdition = dateEdition;
        }

        public void setLangue(String langue) {
            this.langue = langue;
        }

        public void setNombreExemplaires(int nombreExemplaires) {
            this.nombreExemplaires = nombreExemplaires;
        }

        public void setNombreExemplairesDisponibles(int nombreExemplairesDisponibles) {
            this.nombreExemplairesDisponibles = nombreExemplairesDisponibles;
        }
    }

    public static void main(String[] args) {
        Document d1 = new Document("001", "Science", "Physics", "Book", "2020-01-01", "English", 5, 3);
        Document d2 = new Document("002", "Literature", "Poetry", "Magazine", "2019-05-15", "French", 10, 7);
        Document d3 = new Document("003", "Technology", "AI", "Journal", "2021-09-10", "English", 3, 1);

        documents.add(d1);
        documents.add(d2);
        documents.add(d3);

        System.out.println("List of documents in the library:");
        for (Document doc : documents) {
            System.out.println("Code: " + doc.getCode() + ", Discipline: " + doc.getDiscipline() +
                    ", Theme: " + doc.getTheme() + ", Type: " + doc.getType() +
                    ", Date Edition: " + doc.getDateEdition() + ", Language: " + doc.getLangue() +
                    ", Total Copies: " + doc.getNombreExemplaires() + ", Available Copies: " + doc.getNombreExemplairesDisponibles());
        }
    }
}