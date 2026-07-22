student_records = [
        ("Adesina", 85, "Ede"),
        ("Goodnews", 72, "Lagos"),
        ("Chiamaka", 90, "Accra"),
        ("Dayo", 55, "Lagos"),
        ("Emeka", 38, "Kano"),
        ("Samuel", 91, "Lagos"),
        ("Gbenga", 47, "Akure"),
        ("Israel", 68, "Ibadan")
        ]

all_scores = [record[1] for record in student_records]
all_cities = [record[2] for record in student_records]

unique_cities = set(all_cities)

passed = [record[0] for record in student_records if record[1] >= 50]
failed = [record[0] for record in student_records if record[1] < 50]

print("-------------------")
print("Class Report")
print("-------------------")

for name, score, city in student_records:
    status = "PASS" if score >= 50 else "FAIL"
    print(f"{name} ({city}): {score} - {status}")

print("--------------------")
print(f"Total students:     {len(student_records)}")
print(f"Average score:      {round(sum(all_scores)/len(all_scores), 2)}")
print(f"Highest score:      {max(all_scores)}")
print(f"Lowest score:       {min(all_scores)}")
print(f"Cities represented: {len(unique_cities)}")
print(f"Unique cities:      {', '.join(sorted(unique_cities))}")
print(f"Passed:             {len(passed)}")
print(f"Failed:             {len(failed)}")
print("--------------------")














