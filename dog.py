from unicodedata import name


class Dog:
    animal_type = "canine"

    def __init__(self, name) -> None:
        self.name = name


    def bark(self):
        print(self.name + " says woof!")


d1 = Dog(name="Rover")
print(d1.name)
print(d1.animal_type)
d1.bark()
d2 = Dog(name="Ralph")
d2.bark()
