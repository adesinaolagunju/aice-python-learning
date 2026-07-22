def get_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            return (number)
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def calculate(num1, num2, operation):
    if operation == "+":
        return (num1 + num2)
    elif operation == "-":
        return (num1 - num2)
    elif operation == "*":
        return (num1 * num2)
    elif operation == "/":
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return (num1/num2)
    else:
        raise ValueError(f"Unknown operation: {operation}")


print("--------------------")
print("Safe Calculator")
print("--------------------")

num1 = get_number("Enter first number: ")
num2 = get_number("Enter second number: ")
operation = input("Enter operation (+, -, *, /): ")

try:
    result = calculate(num1, num2, operation)
    print(f"Result: {num1} {operation} {num2} = {result}")
except ZeroDivisionError as e:
    print(f"Math Error: {e}")
except ValueError as e:
    print(f"Input Error: {e}")
finally:
    print("--------------------")
    print("Thank you for using Safe Calculator.")
    print("--------------------")













