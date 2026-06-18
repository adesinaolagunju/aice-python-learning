name = input("Enter your name: ")
score = int(input("Enter your score: "))

if score > 70:
    grade = "A"
    message = "Excellent work!"
elif score >= 60:
    grade = "B"
    message = "Good job!"
elif score >=50:
    grade = "C"
    message = "You passed."
elif score >= 40:
    grade = "D"
    message = "You need to improve."
else:
    grade = "F"
    message = "You failed. Please try again."


print("--------------------")
print(f"Name: {name}")
print(f"Score: {score}")
print(f"Grade: {grade}")
print(f"Remark: {message}")
print("--------------------")
