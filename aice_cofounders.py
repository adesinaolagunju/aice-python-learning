cofounders = ["Adesina", "Goodnews", "Samuel", "Israel"]

ages = [26, 25, 32, 30]

print("--------------------")

print("AiCE Community Cofounders")

print("--------------------")

for i in range(len(cofounders)):
    print(f"{cofounders[i]}: {ages[i]} years old")


total = 0

for age in ages:
    total += age

average = total / len(ages)

oldest = max(ages)
youngest = min(ages)


print("--------------------")

print(f"Average age: {average}")
print(f"Oldest cofounder: {oldest}")
print(f"Youngest cofounder: {youngest}")

print("--------------------")
