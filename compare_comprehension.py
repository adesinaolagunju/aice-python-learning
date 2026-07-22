names = ["Adesina", "Goodnews", "Samuel", "Israel", "Chiamaka"]


# Traditional approach
capitalized_traditional = []
for name in names:
    capitalized_traditional.append(name.capitalize())
print(capitalized_traditional)


#List comprehension approach
capitalized_comprehension = [name.capitalize() for name in names]
print(capitalized_comprehension)
