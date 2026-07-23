class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def introduce(self):
        print(f"My name is {self.name}.")
        print(f"I am {self.age} years old.")
        print(f"My email is {self.email}.")


class Teacher(Person):
    def __init__(self, name, age, email, subject):
        super().__init__(name, age, email)
        self.subject = subject

    def introduce(self):
        super().introduce()
        print(f"I teach {self.subject}.")

    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")


class Student(Person):
    def __init__(self, name, age, email, score):
        super().__init__(name, age, email)
        self.score = score

    def introduce(self):
        super().introduce()
        print(f"My score is {self.score}.")

    

teacher1 = Teacher("Mr. Olagunju", 35, "olagunju@school.com", "Python Programming")
student1 = Student("Adesina", 20, "adesina@email.com", 85)

print("--------------------")
teacher1.introduce()
print("--------------------")
student1.introduce()
print("--------------------") 
