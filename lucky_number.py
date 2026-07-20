import random
import datetime

def generate_lucky_numbers(count):
    numbers = []
    for i in range(count):
        number = random.randint(1, 50)
        numbers.append(number)
    return (numbers)

def display_results(name, numbers):
    now = datetime.datetime.now()
    date_str = f"{now.day}/{now.month}/{now.year}"

    print("--------------------")
    print(f"Lucky Numbers for {name}")
    print(f"Date: {date_str}")
    print("--------------------")
    for i, number in enumerate(numbers, 1):
        print(f"Number {i}: {number}")
    print("--------------------")

name = input("Enter your name: ")
lucky = generate_lucky_numbers(5)
display_results(name, lucky) 
