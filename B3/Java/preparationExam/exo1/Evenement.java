public class Evenement {
    private String nomSalle;
    private int nbrPlaces;
    private int billetsReserve = 0;

    public Evenement(String nomSalle, int nbrPlaces) {
        this.nomSalle = nomSalle;
        this.nbrPlaces = nbrPlaces;
    }

    public String toString() {
        return "Événement [Nom de la salle=" + nomSalle + ", Nombre de places=" + nbrPlaces + "]";
    }

    public void setNomSalle(String nomSalle) {
        this.nomSalle = nomSalle;
    }

    public void setBilletsReserve() {
        if (nbrPlaces > this.billetsReserve) {
            this.billetsReserve += 1;
        } else {
            System.out.println("Plus de places disponibles.");
        }
    }

    public void enleverBillet() {
        if (this.billetsReserve > 0) {
            this.billetsReserve -= 1;
        } else {
            System.out.println("Aucun billet réservé à annuler.");
        }
    }

    public void setNbrPlaces(int nbrPlaces) {
        this.nbrPlaces = nbrPlaces;
    }

    public String getNomSalle() {
        return nomSalle;
    }

    public int getNbrPlaces() {
        return nbrPlaces;
    }

    public int getBilletsReserve() {
        return billetsReserve;
    }
}
