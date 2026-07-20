def greet(name):
    return (f"Hello, {name}! Welcom to Python.")

def add(num1, num2):
    return (num1 + num2)

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
