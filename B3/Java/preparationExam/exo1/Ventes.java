
public interface Ventes {
    void reserverBillet(Billet billet, Utilisateur utilisateur);
    void annulerReservation(Billet billet);
    int obtenirBilletsReserves();
}
