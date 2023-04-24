from directeur import*
from personne import*
from educateur import*
from personnelle import* 
def get_objet(self):
    age = self.etudiant.get_age(28)
    prenom = self.etudiant.get_prenom("malik")
    return age,prenom  
john = etudiant("John", "Smith", 16,5) 