class Student:
    def __init__(self, name, age, scores):
        self.name = name
        self.age = age
        self.scores = scores

    def get_average(self):
        return (sum(self.scores)/len(self.scores))

    def get_grade(self):
        average = self.get_average()
        if average >= 70:
            return "A"
        elif average >= 60:
            return "B"
        elif average >= 50:
            return "C"
        elif average >= 40:
            return "D"
        else:
            return "F"

    def display(self):
        average = round(self.get_average(), 2)
        grade = self.get_grade()
        status = "PASS" if average >= 50 else "FAIL"
        print(f"Name:      {self.name}")
        print(f"Age:       {self.age}")
        print(f"Scores:    {self.scores}")
        print(f"Average:   {average}")
        print(f"Grade:     {grade}")
        print(f"Status:    {status}")
        print("--------------------")

students = [
        Student("Adesina", 26, [85, 90, 78, 92]),
        Student("Bola", 22, [55, 48, 62, 50]),
        Student("Chidi", 24, [40, 35, 45, 38]),
        Student("Dayo", 23, [72, 68, 80, 75])
        ]

print("--------------------")
print("Student Management System")
print("--------------------")

for student in students:
    student.display() 
