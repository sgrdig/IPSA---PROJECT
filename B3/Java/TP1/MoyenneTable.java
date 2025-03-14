



public class MoyenneTable {
    private  double[] tableau;

    public MoyenneTable(String[] tableauStr) {
        tableau = new double[tableauStr.length];
        for (int i = 0; i < tableauStr.length; i++) {
            tableau[i] = Double.parseDouble(tableauStr[i]);
        }
    }

    public void affiche() {
        for (double value : tableau) {
            System.out.print(value);
        }}

    public double somme() {
        double sum = 0;
        for (double value : tableau) {
            sum += value;
        }
        return sum;
    }

    public double moyenne() {
        return somme() / tableau.length;
    }

    public static void main(String[] args) {
        String[] tableauStr = {"1.5", "2.3", "3.8", "4.1"};
        MoyenneTable moyenneTable = new MoyenneTable(tableauStr);
        System.out.println("Array elements:");
        moyenneTable.affiche();
        String ch = "Bonjour";
        String ch2 = "Bonjour";
        ch2.equals(ch);
        System.out.println(ch == ch2);
        int n = ch.length();
        char bijour = ch.charAt(n - 1);
        System.out.println(bijour);
        String ch_new = ch.replace("on", "i");
        String ch_no_cap = ch_new.toLowerCase();
        System.out.println(ch_new);
        System.out.println(ch_no_cap);

        String anti_Str = "anticonstitutionnellement";
        char[] tab = {'a', 'e', 'i', 'o', 'u', 'y'};

        for (char e : tab){
            int cpt = 0 ;
            for (int i = 0; i < anti_Str.length(); i++) {
                if (e== anti_Str.charAt(i)){
                    cpt ++;
                }
            
            }
            System.out.println(e + "=" +cpt );

        }}
        
}
