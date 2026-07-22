students = [
        {"name": "Adesina", "score": 85},
        {"name": "Goodnews", "score": 99},
        {"name": "Samuel", "score": 90},
        {"name": "Israel", "score": 55},
        {"name": "Chiamaka", "score": 92},
        {"name": "Funke", "score": 36},
        {"name": "Ajayi", "score": 29},
        {"name": "Gbenga", "score": 48},
        {"name": "Audu", "score": 21}
        ]

all_scores = [student["score"] for student in students]
all_names = [student["name"] for student in students]

passed_students = [student["name"] for student in students if student["score"] >= 50]
failed_students = [student["name"] for student in students if student["score"] < 50]

average = sum(all_scores)/len(all_scores)
highest = max(all_scores)
lowest = min(all_scores)

print("--------------------")
print("Class Results Summary")
print("--------------------")
print(f"Total students: {len(students)}")
print(f"Average score: {round(average, 2)}")
print(f"Highest score: {highest}")
print(f"Lowest score: {lowest}")
print(f"-------------------")
print(f"Passed ({len(passed_students)}): {','.join(passed_students)}")
print(f"Failed ({len(failed_students)}): {','.join(failed_students)}")
print("--------------------") 
