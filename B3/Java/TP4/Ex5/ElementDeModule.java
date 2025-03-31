public class ElementDeModule {
    private String code;
    private String nom;
    private double coefficient;

    public ElementDeModule(String code, String nom, double coefficient) {
        this.code = code;
        this.nom = nom;
        this.coefficient = coefficient;
    }

    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public double getCoefficient() {
        return coefficient;
    }

    public void setCoefficient(double coefficient) {
        this.coefficient = coefficient;
    }

    @Override
    public String toString() {
        return "ElementDeModule{" +
                "code='" + code + '\'' +
                ", nom='" + nom + '\'' +
                ", coefficient=" + coefficient +
                '}';
    }
}