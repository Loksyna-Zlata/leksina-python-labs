import math
def main():
    x = float(input("Введіть x: "))
    if x < 0:
        print("Помилка: x має бути більшим або дорівнювати 0.")
        return
    fx = math.tan(2*x) + math.cos(4*x - (x **(1/2))) - (2 / (abs(x + 1) + 0.1) ** (1/3))
    print("Результат рівняння: ",fx)
main()