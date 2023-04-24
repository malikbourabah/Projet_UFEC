public class professeurs implements ipersonne {
    public String nom;
    public String prenom;
    public String date_naissance;
    private String grade;

    public professeurs() {
    }

    public String getGrade() {
        return this.grade;
    }

    public String getnom() {
        return null;
    }

    public String getprenom() {
        return null;
    }

    public String getdate_naissance() {
        return null;
    }

    public void setnom(String nom) {
    }

    public void setprenom(String prenom) {
    }

    public void setdate_naissance(String date_naissance) {
    }

    public void setGrade(String grade) {
        this.grade = grade;
    }
}

