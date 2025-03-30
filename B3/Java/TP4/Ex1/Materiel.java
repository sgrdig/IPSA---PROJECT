

class Materiel implements Produit {
    private String designation;
    private float prixUnitaire;
    private float quantité;

    public Materiel(String designation, float prixUnitaire, float quantité) {
        this.designation = designation;
        this.prixUnitaire = prixUnitaire;
        this.quantité = quantité;
    }

    @Override
    public String getDesignation() {
        return designation;
    }

    @Override
    public float getPrixUnitaire() {
        return prixUnitaire;
    }

    @Override
    public float getQuantité() {
        return quantité;
    }

    @Override
    public char getNature() {
        return 'M';
    }
}


