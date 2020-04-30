'''
Build on your previous freeform exercise.

Create subclasses of two of the existing classes. Create a subclass of
one of those so that the hierarchy is at least three levels.

Build these classes out like we did in the previous exercises.

If you cannot think of a way to build on your freeform exercise,
you can start from scratch here.

We encourage you to be creative and try to think of an example of
your own for this exercise but if you are stuck, some ideas include:

- A Vehicle superclass, with Truck and Motorcycle subclasses.
- A Restaurant superclass, with Gourmet and FastFood subclasses.

'''


class Person:
    def __init__(self, eyes, hair, poops_per_day):
        self.eyes = eyes
        self.hair = hair
        self.poops_per_day = poops_per_day

    def __str__(self):
        return f"This person likes {self.likes} and poops {self.poops_per_day} times a day"


class Dog:
    def __init__(self, breed, likes, poops_per_day):
        self.breed = breed
        self.likes = likes
        self.poops_per_day = poops_per_day

    def __str__(self):
        return f"This dog likes {self.likes} and poops {self.poops_per_day} times a day"

    def __add__(self, other_dog):
        return int(self.poops_per_day) + int(other_dog.poops_per_day)


class Stray:
    def __init__(self, breed, likes, poops_per_day, home):
        super().__init__(breed,likes, poops_per_day)
        self.home = home


class Mountainier(Person):
    def __init__(self, eyes, hair, poops_per_day, fav_mountain):
        super().__init__(eyes, hair, poops_per_day)
        self.fav_mountain = fav_mountain


class Skier(Mountainier):
    def __init__(self, eyes, hair, poops_per_day, fav_mountain, skis):
        super().__init__(eyes, hair, poops_per_day, fav_mountain)
        self.skis = skis

Brody=Skier("brown", "brown", "2", "Vail", "k2")
print(Brody.skis)