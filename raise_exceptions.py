def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    if age > 150:
        raise ValueError("Age cannot be greater than 150.")
    print(f"Age set to: {age}")

try:
    set_age(26)
    set_age(-5)
except ValueError as e:
    print(f"Error: {e}") 
