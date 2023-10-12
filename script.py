def solve_quadratic(a, b, c):
    d = b * b - 4 * a * c # Discriminant of quadratic equation
    if d < 0:
        return []
    else:
        if d == 0:
            x = -b / (2 * a)
            return [x]
        else:
            x_1 = (-b + d ** 0.5) / (2 * a)
            x_2 = (-b - d ** 0.5) / (2 * a)
            return [x_1, x_2]

print("Определение корней уравнения ax² + bx + c = 0")
a = float(input("Введите число a >>> "))
b = float(input("Введите число b >>> "))
c = float(input("Введите число c >>> "))
print(solve_quadratic(a, b, c))
