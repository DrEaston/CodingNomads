'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets attributes
    to a default value if values are not passed.
- Create at least two objects of each class using the __init__ method.
- Each object should have at least three attributes.
- Each class should have at least two class attributes.
- Create a print method in each class that prints out the attributes
    in a nicely formatted string.
- Include a __str__ method in each class.
- Overload the __add__ method in one of the classes so that it's possible
    to add attributes of two instances of that class using the + operator.
- Once the objects are created, change some of the attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, poker games, sports teams, trees, beers, people etc...


'''


class Person:
    def __init__(self, eyes, hair, language="French", likes="belly rubs", poops_per_day=1):
        self.eyes = eyes
        self.hair = hair
        self.language = language
        self.likes = likes
        self.poops_per_day = poops_per_day

    def __str__(self):
        return f"This person likes {self.likes} and poops {self.poops_per_day} times a day"


class Dog:
    def __init__(self, color, breed, likes="belly rubs", poops_per_day=2):
        self.color = color
        self.breed = breed
        self.likes = likes
        self.poops_per_day = poops_per_day

    def __str__(self):
        return f"This dog likes {self.likes} and poops {self.poops_per_day} times a day"

    def __add__(self, other_dog):
        return int(self.poops_per_day) + int(other_dog.poops_per_day)


class Lizard:
    def __init__(self, color, species, likes="belly rubs", poops_per_day=0.2):
        self.color = color
        self.species = species
        self.poops_per_day = poops_per_day

    def __str__(self):
        return f"This lizard likes {self.likes} and poops {self.poops_per_day} times a day"


Lauren = Person("green", "blonde", "english", "chocolate", 2)
Pierre = Person("brown", "brown")\

Pongo = Dog("white", "jack russell")
Zula = Dog("black", "mutt")
print("Pongo and Zula poop " + str(Pongo+Zula) + " times a day")

Jose = Lizard("green", "iguana")
Juan = Lizard("yellow", "gecko")