from etudiant import*
from service_securite import* 
class director:
    def __init__(self, nom, prenom, age, contact, bio):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.contact = contact
        self.bio = bio
        
    def display_info(self):
        print(f"Nom: {self.nom}")
        print(f"prenom: {self.prenom}")
        print(f"Age: {self.age}")
        print(f"Contact: {self.contact}")
        print(f"bio: {self.bio}")
        
    def get_contact(self):
        print("003763005709")
    def get_bio(self):
        print("Bio of director")    

