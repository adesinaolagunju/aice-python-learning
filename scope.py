def divide (num1, num2):
    if num2 == 0:
        return ("Error: Cannot divide by zero")
    result = num1/num2
    return (result)

print(divide(10, 2))
print(divide(10, 0)) 
