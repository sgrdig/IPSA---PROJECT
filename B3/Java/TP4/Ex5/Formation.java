import java.util.List;

public class Formation {
    private List<Semestre> semestres;
    private List<Etudiant> etudiants ;

    public Formation(List<Semestre> semestres ,List<Etudiant> etudiants  ) {
        this.semestres = semestres;
        this.etudiants =  etudiants;
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

    public List<Etudiant> getEtudiants() {
        return etudiants;
    }

    public void setEtudiants(List<Etudiant> etudiants) {
        this.etudiants = etudiants;
    }
}
// add list etudiant