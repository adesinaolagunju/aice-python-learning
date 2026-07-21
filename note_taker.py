import datetime

def add_note(note):
    now = datetime.datetime.now()
    timestamp = f"{now.day}/{now.month}/{now.year} {now.hour}:{now.minute}"
    with open("my_notes.txt", "a") as file:
        file.write(f"[{timestamp}] {note}\n")
    print("Note saved.")

def view_notes():
    try:
        with open("my_notes.txt", "r") as file:
            lines = file.readlines()
        if len(lines) == 0:
            print("No notes yet.")
        else:
            print("--------------------")
            print("Your Notes")
            print("--------------------")
            for line in lines:
                print(line.strip())
            print("--------------------")
    except FileNotFoundError:
        print("No notes file found. Add a note first.")

print("1. Add a note")
print("2. View notes")

choice = input("Enter your choice: ")

if choice == "1":
    note = input("Enter your note: ")
    add_note(note)
elif choice == "2":
    view_notes()
else:
    print("Invalid choice.")   
