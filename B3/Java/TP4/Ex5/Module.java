import java.util.List;

public class Module {
    private String code;
    private String nom;
    private List<Module> preRequis;
    private List<ElementDeModule> elements;

    public Module(String code, String nom, List<Module> preRequis, List<ElementDeModule> elements) {
        this.code = code;
        this.nom = nom;
        this.preRequis = preRequis;
        this.elements = elements;
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

    public List<Module> getPreRequis() {
        return preRequis;
    }

    public void setPreRequis(List<Module> preRequis) {
        this.preRequis = preRequis;
    }

    public List<ElementDeModule> getElements() {
        return elements;
    }

    public void setElements(List<ElementDeModule> elements) {
        this.elements = elements;
    }

    @Override
    public String toString() {
        return "Module{" +
                "code='" + code + '\'' +
                ", nom='" + nom + '\'' +
                '}';
    }
}