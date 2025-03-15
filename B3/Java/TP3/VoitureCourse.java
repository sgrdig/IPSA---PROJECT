public class VoitureCourse extends Voiture {
    private boolean aileron;

    public VoitureCourse(String marque, String[] options, boolean aileron) {
        super(marque, options, 250);
        this.aileron = aileron;
    }

    @Override
    public void affiche() {
        super.affiche();
        if (aileron) {
            System.out.println("Je suis une voiture de course avec aileron");
        } else {
            System.out.println("Je suis une voiture de course sans aileron");
        }
    }

    @Override
    public void demarrer() {
        super.demarrer();
        System.out.println("Vrouuum");
    }

    public static void main(String[] args) {
        String[] options = {"Option1", "Option2"};
        VoitureCourse voiture = new VoitureCourse("Ferrari", options, true);
        voiture.affiche();
        voiture.demarrer();
    }
}