# FileNotFoundError - trying to open a file that does not exist
try:
    with open("missing_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: The file does not exist.")


# IndexError - trying to access an index that is out of range
try:
    fruits = ["mango", "orange", "banana"]
    print(fruits[10])
except IndexError:
    print("Error: That index does not exist in the list.")


# KeyError - trying to access a key that does not exist in a dictionary
try:
    student = {"name": "Adesina", "age": 26}
    print(student["score"])
except KeyError:
    print("Error: That key does not exist in the dictionary.") 

