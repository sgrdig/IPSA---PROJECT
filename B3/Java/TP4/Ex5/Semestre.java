import java.util.List;

public class Semestre {
    private int numero;
    private List<Module> modules;

    public Semestre(int numero, List<Module> modules) {
        this.numero = numero;
        this.modules = modules;
    }

    public int getNumero() {
        return numero;
    }

    public void setNumero(int numero) {
        this.numero = numero;
    }

    public List<Module> getModules() {
        return modules;
    }

    public void setModules(List<Module> modules) {
        this.modules = modules;
    }

    @Override
    public String toString() {
        return "Semestre{" +
                "numero=" + numero +
                ", modules=" + modules +
                '}';
    }
}