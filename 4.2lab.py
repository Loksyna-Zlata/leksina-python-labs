import math
def calculate_u(x, y):
    U = x * math.log10(y) + (1 / (x ** 2 + y ** 2 + 0.3)) - math.exp(6 * x - y)
    return U
def main ():
    x = float(input("Введіть x: "))
    y = float(input("Введіть y: "))
    if y <= 0:
        print("Помилка: y має бути більшим за 0.")
        return
    U = calculate_u (x, y)
    print("Результат U = ", U)
main ()