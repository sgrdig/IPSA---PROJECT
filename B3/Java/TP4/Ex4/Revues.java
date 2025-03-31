public class Revues {
    private String modeParution;
    private final String auteur;

    // Constructor
    public Revues(String auteur, String modeParution) {
        this.auteur = auteur;
        this.modeParution = modeParution;
    }

    // Getter
    public String getModeParution() {
        return modeParution;
    }

    // Setter
    public void setModeParution(String modeParution) {
        this.modeParution = modeParution;
    }

    // Getter for auteur
    public String getAuteur() {
        return auteur;
    }
}