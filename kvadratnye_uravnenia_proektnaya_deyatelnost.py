print("Уравнение ax² + bx + c = 0")
a = int(input("Введите a "))
b = int(input("Введите b "))
c = int(input("Введите c "))
def quadrat_equasion(a, b, c):
    D = b ** 2 - 4 * a * c
    if D < 0:
        print("У этого уравнения существуют только мнимые корни.")
    else:
        x1 = (-b + D ** 0.5) / (2 * a)
        x2 = (-b - D ** 0.5) / (2 * a)
        if x1 == x2:
            print(f"x1 = {x1}")
        else:   
            print(f"x1 = {x1}, x2 = {x2}")
