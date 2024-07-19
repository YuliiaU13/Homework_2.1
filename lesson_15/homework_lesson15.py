"""
Створіть абстрактний клас "Фігура" з абстрактиними методами
для отримання площі та периметру.
Наслідуйте від нього декілька (> 2) інших фігур,
та реалізуйте математично вірні для них методи для площі та периметру.
Властивості по типу “довжина сторони” и тд повинні бути приватними,
та ініціалізуватись через конструктор.
Створіть Декілька різних об’єктів фігур,
та у циклі порахуйте та виведіть в консоль площу та периметр кожної.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def perimeter(self):
        return 2 * math.pi * self.__radius

    def area(self):
        return math.pi * (self.__radius ** 2)


class Rectangle(Shape):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def perimeter(self):
        return 2 * (self.__length + self.__width)

    def area(self):
        return self.__length * self.__width


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def perimeter(self):
        return self.__a + self.__b + self.__c

    def area(self):
        p = (self.__a + self.__b + self.__c) / 2
        return math.sqrt(p * (p - self.__a) * (p - self.__b) * (p - self.__c))


figure_1 = Circle(radius=11)
figure_2 = Rectangle(length=4, width=8)
figure_3 = Triangle(a=3, b=4, c=5)

shapes = [figure_1, figure_2, figure_3]

for shape in shapes:
    print(f"{shape.__class__.__name__} perimeter: {shape.perimeter():.2f}")
    print(f"{shape.__class__.__name__} area: {shape.area():.2f}")