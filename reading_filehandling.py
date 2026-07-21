file = open("notes.txt", "r")
lines = file.readlines()
file.close()

for line in lines:
    print(line.strip()) 
