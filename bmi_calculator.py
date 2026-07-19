def calculate_bmi (weight, height):
    if height <= 0 or weight <= 0:
        return (None, "Error: Weight and height must be greater than zero.")
    bmi = weight / (height ** 2)
    bmi = round(bmi, 2)
    return (bmi, None)

def get_category(bmi):
    if bmi < 18.5:
        return ("Underweight")
    elif bmi < 25.0:
        return ("Normal weight")
    elif bmi < 30.0:
        return ("Overweight")
    else:
        return ("Obese")

name = input("Enter your name: ")
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi, error = calculate_bmi(weight, height)

if error:
    print(error)
else:
    category = get_category(bmi)
    print("--------------------")
    print(f"Name:     {name}")
    print(f"BMI:      {bmi}")
    print(f"Category: {category}")
    print("--------------------")
