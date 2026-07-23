class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def update_score(self, new_score):
        self.score = new_score
        print(f"{self.name}'s score has been updated to {self.score}.")

student1 = Student("Adesina", 26, 85)
student2 = Student("Bola", 22, 72)

print(f"Before: {student1.name} - {student1.score}")
print(f"Before: {student2.name} - {student2.score}")

student1.update_score(92)

print(f"After: {student1.name} - {student1.score}")
print(f"After: {student2.name} - {student2.score}") 
