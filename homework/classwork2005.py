# Створити батьківський клас Figure з методами __init__: ініціалізується колір,
# get_color: повертає колір фігури,
# info: надає інформацію про фігуру та колір,
# від якого наслідуються такі класи як Rectangle,
# Square, які мають інформацію про ширину,
# висоту фігури, метод square, який знаходить площу фігури.

class Figure:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return "The color of figure is {}".format(self.color)

    def info(self):
        return "This is figure - and the color of figure is {}".format(self.color)


class Rectangle(Figure):
    def __init__(self, color):
        Figure.__init__(self, color)
        self.a = float(input("Enter height of rectangle: "))
        self.b = float(input("Enter width of rectangle: "))


    def square_of_rectangle(self):
        return "The S of rectangle = a * b = {}".format(self.a * self.b)


class Square(Figure):
    def __init__(self, color):
        Figure.__init__(self, color)
        self.a = float(input("Enter side of square: "))

    def sguare_of_square(self):
        return "The S of square = a ** 2 = {}".format(self.a ** 2)

f = Figure("black")
print(f.info())
print(f.get_color())
rect = Rectangle("black")
print(rect.square_of_rectangle())
sqr = Square("white")
print(sqr.sguare_of_square())

