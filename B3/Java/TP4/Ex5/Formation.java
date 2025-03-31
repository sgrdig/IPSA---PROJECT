import java.util.List;

public class Formation {
    private List<Semestre> semestres;

    public Formation(List<Semestre> semestres) {
        this.semestres = semestres;
    }

    public void ajouterSemestre(Semestre semestre) {
        this.semestres.add(semestre);
    }

    public List<Semestre> getSemestres() {
        return semestres;
    }

    public void setSemestres(List<Semestre> semestres) {
        this.semestres = semestres;
    }

    @Override
    public String toString() {
        return "Formation{" +
                "semestres=" + semestres +
                '}';
    }
}