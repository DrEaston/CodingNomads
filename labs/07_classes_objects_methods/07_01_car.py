'''
Write a class to model a car. The class should:

1. Set the attributes model, year, and max_speed in the __init__() method.
2. Have a method that increases the max_speed of the car by 5 when called.
3. Have a method that prints the details of the car.

Create at least two different objects of this Car class and demonstrate
changing the objects attributes.

'''

class Car():
    def __init__(self, model, year, max_speed=100):
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def __str__(self):
        return f"Car is a {self.year}, {self.model} with top speed {self.max_speed} mph"

    def boost(self):
        self.max_speed += 5

x=Car("Mercury", 1966, 144)
print(x)
x.boost()
print(x)