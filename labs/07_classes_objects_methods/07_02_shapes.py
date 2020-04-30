'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''


class Circle:
    def __init__(self, radius=4):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class Square:
    def __init__(self, side=4):
        self.side = side

    def area(self):
        return self.side ** 2


x = Square(6)
print(x.area())
y = Circle(5)
print(y.area())
