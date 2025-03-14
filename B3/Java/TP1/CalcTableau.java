public class CalcTableau {

    public static double somme(double[] tableau) {
        double sum = 0;
        for (double value : tableau) {
            sum += value;
        }
        return sum;
    }

    public static void increment(double[] tableau, double valeur) {
        for (int i = 0; i < tableau.length; i++) {
            tableau[i] += valeur;
        }
    }

    public static void affiche(double[] tableau) {
        for (double value : tableau) {
            System.out.print(value + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        double[] tableau = {1.1, 2.2, 3.3, 4.4};
        System.out.println("Sum: " + CalcTableau.somme(tableau));
        CalcTableau.increment(tableau, 1.0);
        CalcTableau.affiche(tableau);
        CalcTableau.affiche(tableau);
    }
}
