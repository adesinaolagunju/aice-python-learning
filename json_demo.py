import json

students = {
        "name": "Adesina",
        "age": 26,
        "country": "Nigeria",
        "scores": [85, 90, 78],
        "is_student": True
        }

json_string = json.dumps(students, indent=4)

print(json_string)
print(type(json_string)) 
