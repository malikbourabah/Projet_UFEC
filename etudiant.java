public class etudiant {
    public String nom;
    public String prenom;
    public String date_naissance;
    private String Classe;

    public etudiant(String nom, String prenom, String date_naissance, String classe) {
        this.nom = nom;
        this.prenom = prenom;
        this.date_naissance = date_naissance;
        this.classe = classe;
}
    public String getClasse() {
        return this.classe;
    }

    public String getnom() {
        return this.nom;
    }

    public String getprenom() {
        return this.prenom;
    }

    public String getdate_naissance() {
        return this.date_naissance;
    }

    public void setnom(String nom) {
        this.nom = nom;
    }

    public void setprenom(String prenom) {
        this.prenom = prenom;
    }

    public void setdate_naissance(String date_naissance) {
        this.date_naissance = date_naissance;
    }

    public void setclasse(String Classe) {
        this.Classe = Classe;
    }
}
