import json

students = [
        {"name": "Adesina", "age": 20, "score": 85},
        {"name": "Bola", "age": 22, "score": 72},
        {"name": "Chidi", "age": 21, "score": 55},
        {"name": "Dayo", "age": 23, "score": 55},
        {"name": "Emeka", "age": 20, "score": 38}
        ]

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

print("students.json written successfully.")

with open("students.json", "r") as file:
    loaded_students = json.load(file)

print(f"Total students loaded: {len(loaded_students)}")
print("-------------------")

for student in loaded_students:
    print(f"Name: {student['name']}, Age: {student['age']}, Score: {student['score']}") 
