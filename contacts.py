contacts = [
        {"name": "Adesina", "phone": "08103230934", "city": "Ede"},
        {"name": "Goodnews", "phone": "08034631249", "city": "Lagos"},
        {"name": "Samuel", "phone": "07033355403", "city": "Lagos"},
        {"name": "Israel", "phone": "08116441012", "city": "Ibadan"}
        ]


print("--------------------")
print("Contact Book")
print("--------------------")

for contact in contacts:
    print(f"Name: {contact['name']}")
    print(f"Phone: {contact['phone']}")
    print(f"City: {contact['city']}")
    print("--------------------")

search = input("Enter a name to search: ")

found = False

for contact in contacts:
    if contact["name"] == search:
        print("Contact found!")
        print(f"Name: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"City: {contact['city']}")
        found = True

if not found:
    print("Contact not found.") 
