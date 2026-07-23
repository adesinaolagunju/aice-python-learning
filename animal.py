class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        print(f"{self.name} says {self.sound}.")

    def describe(self):
        print(f"I am an animal called {self.name}.")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Woof")

    def fetch(self):
        print(f"{self.name} fetches the ball!")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Meow")

    def purr(self):
        print(f"{self.name} is purring...")


class Cow(Animal):
    def __init__(self, name):
        super().__init__(name, "Moo")

    def give_milk(self):
        print(f"{self.name} gives milk.")


dog = Dog("Rex")
cat = Cat("Whiskers")
cow = Cow("Daisy")

animals = [dog, cat, cow]

for animal in animals:
    animal.describe()
    animal.speak()
    print("--------------------")



