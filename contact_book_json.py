import json
import os

FILENAME = "contacts.json"

def load_contacts():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return []

def save_contacts(contacts):
    with open(FILENAME, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(name, phone, email, city):
    contacts = load_contacts()
    contact = {
            "name": name,
            "phone": phone,
            "email": email,
            "city": city
            }
    contacts.append(contact)
    save_contacts(contacts)
    print(f"Contact '{name}' saved successfully.")

def view_contacts():
    contacts = load_contacts()
    if len(contacts) == 0:
        print("No contacts found.")
        return
    print("--------------------")
    print("All Contacts")
    print("--------------------")

    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['name']}")
        print(f"   Phone: {contact['phone']}")
        print(f"   Email: {contact['email']}")
        print(f"   City:  {contact['city']}")
        print("-------------------")

def search_contact(search_name):
    contacts = load_contacts()
    found = False
    for contact in contacts:
        if contact["name"].lower() == search_name.lower():
            print("--------------------")
            print("Contact Found:")
            print(f"Name:  {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"City:  {contact['city']}")
            print("--------------------")
            found = True
        if not found:
            print(f"No contact found with the name '{search_name}'.")

print("--------------------")
print("JSON Contact Book")
print("--------------------")
print("1. Add contact")
print("2. View all contacts")
print("3. Search contact")
print("--------------------")

choice = input("Enter your choice: ")

if choice == "1":
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    city = input("City: ")
    add_contact(name, phone, email, city)
elif choice == "2":
    view_contacts()
elif choice == "3":
    name = input("Enter name to search: ")
    search_contact(name)
else:
    print("Invalid choice.") 








