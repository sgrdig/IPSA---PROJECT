
public class ReservationPlace {
    private Utilisateur user;
    private Billet billet;
    private Evenement evenement;

    public ReservationPlace(Utilisateur user, Billet billet, Evenement evenement) {
        this.user = user;
        this.billet = billet;
        this.evenement = evenement;
    }

    public void reserveBillet(Billet billet, Utilisateur user) {
        billet.setUser(user); // Réserver le billet pour l'utilisateur
        evenement.setBilletsReserve(); // Mettre à jour le nombre de billets réservés pour l'événement
        System.out.println("Billet réservé pour l'utilisateur " + user.getNom() + " " + user.getPrenom());
    }

    public void cancelBillet() {
        billet.rmUser(); // Annuler la réservation
        evenement.enleverBillet(); // Mettre à jour le nombre de billets réservés pour l'événement
        System.out.println("Billet annulé pour l'utilisateur " + user.getNom() + " " + user.getPrenom());
    }
}
