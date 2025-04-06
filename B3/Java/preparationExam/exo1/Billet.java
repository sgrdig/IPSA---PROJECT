public class Billet {
    private int prix;
    private boolean type; // False = Standard, True = VIP
    private boolean status; // False = disponible, True = réservé
    private Utilisateur user;
    private static int compteurId = 0; // Compteur pour générer des IDs uniques
    private int id;

    public Billet(int prix, boolean type, boolean status) {
        this.id = ++compteurId; // Incrémenter l'ID à chaque nouveau billet
        this.prix = prix;
        this.type = type;
        this.status = status;
        this.user = null; // Pas d'utilisateur initialement
    }

    public void setUser(Utilisateur user) {
        if (this.status == false) { // Vérifie que le billet est disponible
            this.user = user;
            this.status = true;  // Le billet devient réservé
        } else {
            System.out.println("Le billet est déjà réservé.");
        }
    }

    public void rmUser() {
        if (this.status == true) { // Billet réservé, on peut supprimer l'utilisateur
            this.user = null;
            this.status = false;  // Le billet redevient disponible
            System.out.println("Utilisateur supprimé et billet rendu disponible.");
        } else {
            System.out.println("Le billet n'était pas réservé.");
        }
    }

    public int getPrix() {
        return prix;
    }

    public boolean isType() {
        return type;
    }

    public boolean isStatus() {
        return status;
    }

    public Utilisateur getUser() {
        return user;
    }

    public void setPrix(int prix) {
        this.prix = prix;
    }

    public void setType(boolean type) {
        this.type = type;
    }

    public void setStatus(boolean status) {
        this.status = status;
    }

    public int getId() {
        return id;
    }
}
