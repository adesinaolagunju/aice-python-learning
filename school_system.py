class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def get_info(self):
        return (f"{self.name} | Age: {self.age} | Email: {self.email}")

class Teacher(Person):
    def __init__(self, name, age, email, subject, salary):
        super().__init__(name, age, email)
        self.subject = subject
        self.salary = salary

    def get_info(self):
        base = super().get_info()
        return (f"{base} | Subject: {self.subject} | Salary: #{self.salary}")

    def teach(self):
        print(f"{self.name} is now teaching {self.subject}. Please pay attention.")


class Student(Person):
    def __init__(self, name, age, email, scores):
        super().__init__(name, age, email)
        self.scores = scores

    def get_average(self):
        return (round(sum(self.scores) / len(self.scores), 2))

    def get_grade(self):
        avg = self.get_average()
        if avg >= 70:
            return "A"
        elif avg >= 60:
            return "B"
        elif avg >= 50:
            return "C"
        elif avg >= 40:
            return "D"
        else:
            return "F"

    def get_info(self):
        base = super().get_info()
        return (f"{base} | Average: {self.get_average()} | Grade: {self.get_grade()}")


class Admin(Person):
    def __init__ (self, name, age, email, department):
        super().__init__(name, age, email)
        self.department = department

    def get_info(self):
        base = super().get_info()
        return (f"{base} | Department: {self.department}")

teachers = [
        Teacher("Mr. Olagunju", 35, "olagunju@school.com", "Python Programming", 150000),
        Teacher("Mrs. Adeyemi", 40, "adeyemi@school.com", "Mathematics", 140000)
        ]

students = [
        Student("Adesina", 20, "adesina@email.com", [85, 90, 78]),
        Student("Bola", 22, "bola@email.com", [55, 48, 62]),
        Student("Chidi", 21, "chidi@email.com", [40, 35, 45])
        ]

admin = Admin("Mrs. Okafor", 45, "okafor@school.com", "Administration")

print("====================")
print("SCHOOL MANAGEMENT SYSTEM")
print("====================")

print("\nTEACHERS:")
print("--------------------")
for teacher in teachers:
    print(teacher.get_info())

print("\nSTUDENTS")
print("--------------------")
for student in students:
    print(student.get_info())

print("\nADMIN")
print("--------------------")
print(admin.get_info())

print("\n--------------------")
teachers[0].teach()
print("--------------------") 



















