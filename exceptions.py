try:
    number = int(input("Enter a number: "))
    result = 10/number
    print(f"Result: {result}") 
except ValueError:
    print("Invalid input. Please enter a number, not a word") 
except ZeroDivisionError:
    print("You cannot divide by zero. Please enter a different number.")
else:
    print(f"Success! The result is: {result}")
finally:
    print("Program finished.") 
