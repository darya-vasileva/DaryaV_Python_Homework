import math


def square(side):
    return math.ceil(side * side)


side_of_square = float(input("Сторона квадрата: "))
print(f"Площадь квадрата: {square(side_of_square)}")
