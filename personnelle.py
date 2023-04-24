class personelle:
    def _ini_(self, nom, prenom, age, tache):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.tache = tache
    def display_info(self):
        print(f"Nom: {self.nom}")
        print(f"prenom: {self.prenom}")
        print(f"Tache: {self.tache}")
    def get_personelle(self):
        print("La tache de monsieur est")