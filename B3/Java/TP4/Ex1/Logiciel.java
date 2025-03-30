

class Logiciel implements Produit {
    private String designation;
    private float prixUnitaire;
    private float quantité;
    private String editeur;
    private int anneeEdition;

    public Logiciel(String designation, float prixUnitaire, float quantité, String editeur, int anneeEdition) {
        this.designation = designation;
        this.prixUnitaire = prixUnitaire;
        this.quantité = quantité;
        this.editeur = editeur;
        this.anneeEdition = anneeEdition;
    }

    
    public String getDesignation() {
        return designation;
    }

    
    public float getPrixUnitaire() {
        return prixUnitaire;
    }

   
    public float getQuantité() {
        return quantité;
    }

   
    public char getNature() {
        return 'L';
    }

    public String getEditeur() {
        return editeur;
    }

    public int getAnneeEdition() {
        return anneeEdition;
    }

   
    public float prixUnitaire() {
        throw new UnsupportedOperationException("Not supported yet.");
    }

    @Override
    public float getQuantite() {
        throw new UnsupportedOperationException("Not supported yet.");
    }
}
