class etudiant:
    def __init__(self, nom, prenom, age, classe):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.classe = classe
        
    def display_info(self):
        print(f"Nom: {self.nom}")
        print(f"prenom: {self.prenom}")
        print(f"Age: {self.age}")
        print(f"Classe: {self.classe}")
        
    def get_classe_level(self):
        if self.grade >= 5:
            print("master deuxieme année")
        elif self.grade >= 4:
            print("master premiere année")
        else:
            print("etudiant en cycle licence")
