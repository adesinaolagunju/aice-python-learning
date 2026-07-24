from tabulate import tabulate

students = [
        ["Adesina", 25, 85, "A"],
        ["Bola", 22, 72, "B"],
        ["Chidi", 24, 90, "A"],
        ["Dayo", 23, 55, "C"],
        ["Emeka", 21, 38, "F"]
        ]

headers = ["Name", "Age", "Score", "Grade"]

print(tabulate(students, headers=headers, tablefmt="fancy_grid")) 
