public class Concession {
    private Voiture[] stock;

    public Concession(Voiture voiture) {
        this.stock = new Voiture[1];
        this.stock[0] = voiture;
    }

    public void ajoutVoiture(Voiture voiture) {
        Voiture[] nouveauStock = new Voiture[stock.length + 1];
        for (int i = 0; i < stock.length; i++) {
            nouveauStock[i] = stock[i];
        }
        nouveauStock[stock.length] = voiture;
        stock = nouveauStock;
    }

    public void affiche() {
        System.out.println("Le stock:");
        for (int i = 0; i < stock.length; i++) {
            System.out.println("Voiture num " + i);
            stock[i].affiche();
        }
    }

    public void rechercheOptions(String option) {
        System.out.println("Voitures en stock avec l'option " + option);
        for (int i = 0; i < stock.length; i++) {
            Voiture voiture = stock[i];
            for (int j = 0; j < voiture.options.length; j++) {
                if (voiture.options[j].equals(option)) {
                    voiture.affiche();
                    break;
                }
            }}}
        public static void main(String[] args) {
        String[] op1 = {"ABS", "GPS"};
        String[] op2 = {"ABS", "autoradio", "jantes alu"};
        String[] op3 = {"GPS", "sieges cuir"};

        Voiture v1 = new Voiture("Audi", op1, 120);
        Voiture v2 = new Voiture("Peugeot", op2, 80);

        VoitureCourse v3 = new VoitureCourse("BMW", op3, true);

        v1.demarrer();
        v3.demarrer();

        Concession c = new Concession(v1);
        c.ajoutVoiture(v2);
        c.ajoutVoiture(v3);
        c.affiche();
        c.rechercheOptions("GPS");
    }
}
