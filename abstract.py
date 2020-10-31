from abc import ABC


class Shape(ABC):
    def calcArea(self):
        pass


class Rectangle(Shape):
    length = 4
    width = 3

    def calcArea(self):
        return self.length * self.width


class Circle(Shape):
    radius = 4

    def calcArea(self):
        return 3.14 * self.radius * self.radius


rec = Rectangle()
cir = Circle()
print("Area of this rectangle:", rec.calcArea())
print("Area of this circle:", cir.calcArea())