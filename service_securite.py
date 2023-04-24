class service_securite:
    def __init__(self, nom, prenom, mission):
        self.nom = nom
        self.prenom = prenom
        self.mission = mission
        
    def display_info(self):
        print(f"Nom: {self.nom}")
        print(f"prenom: {self.prenom}")
        print(f"Mission: {self.mission}")
       
        
    def get_mission(self):
        if self.mission >= 3:
            print("sécurité porte portes principale")
        elif self.mission >= 2:
            print("sécurité interieur de l'etablissement")
        else:
            print("sécurité incendie")
