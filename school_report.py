from colorama import Fore, Style
from tabulate import tabulate
import colorama

colorama.init()

students = [
        {"name": "Adesina", "age": 20, "scores": [85, 90, 78]},
        {"name": "Bola", "age": 22, "scores": [55, 48, 62]},
        {"name": "Chidi", "age": 21, "scores": [90, 95, 88]},
        {"name": "Dayo", "age": 23, "scores": [40, 35, 45]},
        {"name": "Emeka", "age": 20, "scores": [72, 68, 75]}
        ]

def get_grade(average):
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

table_data = []

for student in students:
    average = round(sum(student["scores"])/len(student["scores"]), 2)
    grade = get_grade(average)
    status = "PASS" if average >= 50 else "FAIL"
    table_data.append([student["name"], student["age"], average, grade, status])

headers = ["Name", "Age", "Average", "Grade", "Status"]

print(Fore.CYAN + "="*50)
print("               SCHOOL REPORT CARD")
print("="*50 + Style.RESET_ALL)

print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))

all_averages = [row[2] for row in table_data]
passed = [row for row in table_data if row[4] == "PASS"]
failed = [row for row in table_data if row[4] == "FAIL"]

print(Fore.CYAN + "\nSUMMARY:" + Style.RESET_ALL)
print(f"Total Students: {len(students)}")
print(Fore.GREEN + f"Passed: {len(passed)}" + Style.RESET_ALL)
print(Fore.RED + f"Failed: {len(failed)}" + Style.RESET_ALL)
print(f"Class Average: {round(sum(all_averages)/len(all_averages), 2)}")














