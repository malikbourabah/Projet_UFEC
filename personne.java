public class personne implements interface_ecole {
    public String nom;
    public String prenom;
    public String date_naissance;

    public personne(String nom, String prenom, String date_naissance) {
        this.nom = nom;
        this.prenom = prenom;
        this.date_naissance = date_naissance;
    }

    public String getnom() {
        return this.nom;
    }

    public String getprenom() {
        return this.prenom;
    }

    public void setnom(String nom) {
        this.nom = nom;
    }

    public void setprenom(String prenom) {
        this.prenom = prenom;
    }

    public String getdate_naissance() {
        return this.date_naissance;
    }

    public void setdate_naissance(String date_naissance) {
        this.date_naissance = date_naissance;
    }
}
