class educateur:
    def _init_(self, nom, prenom, age, grade):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.grade = grade
    def display_info(self):
        print(f"Nom: {self.nom}")
        print(f"prenom: {self.prenom}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")
    def get_grade_level(self):
        if self.grade >= 5:
            print("enseignant chercheur")
        elif self.grade >= 4:
            print("professeur")
        else:
            print("remplaçant")