def get_grade(score):
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "F"

def get_remark(grade):
    if grade == "A":
        return "Excellent!"
    elif grade == "B":
        return "Good job!"
    elif grade == "C":
        return "You passed."
    elif grade == "D":
        return "You need to improve."
    else:
        return "You failed. Please try again."


def print_result(name, score):
    grade = get_grade(score)
    remark = get_remark(grade)
    print("--------------------")
    print(f"Name: {name}")
    print(f"Score: {score}")
    print(f"Grade: {grade}")
    print(f"Remark: {remark}")
    print("--------------------")


print_result("Adesina", 85)
print_result("Chiamaka", 62)
print_result("Chidi", 45)
print_result("Dayo", 30) 
