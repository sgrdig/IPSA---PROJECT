import java.util.LinkedList;
import java.util.List;

class GestionDeStock {
    private LinkedList<Produit> stock;

    
    public GestionDeStock() {
        stock = new LinkedList<Produit>();
    }

    public void ajouter(Produit produit) {
        stock.add(produit);
    }

    public void lister() {
        for (Produit produit : stock) {
            System.out.println("Désignation: " + produit.getDesignation());
            System.out.println("Prix Unitaire: " + produit.getPrixUnitaire());
            System.out.println("Quantité: " + produit.getQuantité());
            System.out.println("Nature: " + produit.getNature());
            if (produit instanceof Logiciel) {
                Logiciel logiciel = (Logiciel) produit;
                System.out.println("Editeur: " + logiciel.getEditeur());
                System.out.println("Année d'Edition: " + logiciel.getAnneeEdition());
            }
            System.out.println();
        }
    }

    public void supprimer(Produit produit) {
        stock.remove(produit);
    }

    public Produit rechercherParDesignation(String designation) {
        for (Produit produit : stock) {
            if (produit.getDesignation().equals(designation)) {
                return produit;
            }
        }
        return null;
    }
}