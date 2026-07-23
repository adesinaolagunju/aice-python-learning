class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def get_grade(self):
        if self.score >= 70:
            return "A"
        elif self.score >= 60:
            return "B"
        elif self.score >= 50:
            return "C"
        elif self.score >= 40:
            return "D"
        else:
            return "F"

    def introduce(self):
        grade = self.get_grade()
        print(f"My name is {self.name}")
        print(f"I am {self.age} years old.")
        print(f"My score is {self.score} and my grade is {grade}.")


student1 = Student("Adesina", 26, 85)
student2 = Student("Bola", 22, 42)


student1.introduce()
print("--------------------")
student2.introduce() 
