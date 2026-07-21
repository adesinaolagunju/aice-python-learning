file = open("notes.txt", "a")
file.write("This line was appended.\n")
file.write("This line was also appended.\n")
file.close()

print("Lines appended successfully.") 
