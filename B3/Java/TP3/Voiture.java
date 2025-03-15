    class Voiture {
        public String marque;
        public int nbchevaux;
        public String[] options;

        public Voiture(String marque, String[] options, int nbchevaux) {
            this.marque = marque;
            this.nbchevaux = nbchevaux;
            this.options = new String[options.length];
            for(int i = 0; i < options.length; i++) {
                this.options[i] =  options[i];
            }
        }

        public void affiche() {
            System.out.println("Marque: " + marque + ", Nombre de chevaux: " + nbchevaux);
            System.out.print("Options: ");
            for (String option : options) {
                System.out.print(option + " ");
            }
            System.out.println();
        }

        public void demarrer() {
            System.out.println("Demarrage OK");
                }


    }

