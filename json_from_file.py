import json

student = {
        "name": "Adesina",
        "age": 26,
        "country": "Nigeria",
        "scores": [85, 90, 78],
        "is_student": True
        }

with open ("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("JSON file written successfully.")

with open("student.json", "r") as file:
    loaded_student = json.load(file)

print(loaded_student)
print(f"Name: {loaded_student['name']}")
print(f"Country: {loaded_student['country']}")
print(f"Scores: {loaded_student['scores']}") 
