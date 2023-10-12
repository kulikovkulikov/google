from math import sqrt

def solve_quadratic(a, b, c):
    if(a == 0) 
    d = b * b - 4 * a * c # Discriminant of quadratic equation
    if d < 0:
        return []
    else:
        if d == 0:
            x = -b / (2 * a)
            return [x]
        else:
            x_1 = (-b + sqrt(d)) / (2 * a)
            x_2 = (-b - sqrt(d)) / (2 * a)
            return [x_1, x_2]

print("Определение корней уравнения ax² + bx + c = 0")
a = float(input("Введите число a >>> "))
b = float(input("Введите число b >>> "))
c = float(input("Введите число c >>> "))
print(quadratic_equation(a, b, c))
