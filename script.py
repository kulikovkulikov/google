def solve_quadratic(a, b, c):
    d = b * b - 4 * a * c # Discriminant of quadratic equation
    if d < 0:
        return []
    elif d == 0:
        x = -b / (2 * a)
        return [x]
    else:
        x_1 = (-b + d ** 0.5) / (2 * a)
        x_2 = (-b - d ** 0.5) / (2 * a)
        return [x_1, x_2]

print('Определение корней уравнения ax² + bx + c = 0')

a = float(input('Введите число a >>> '))
b = float(input('Введите число b >>> '))
c = float(input('Введите число c >>> '))

x = solve_quadratic(a, b, c)

if len(x) == 0:
    print('Нет действительных корней')
elif len(x) == 1:
    print('x =', x[0])
else:
    print('x_1 = ', x[0], ', x_2 = ', x[1], sep='')
