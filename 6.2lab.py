import math
a = int(input("Введіть a: "))
b = float(input("Введіть b: "))
h = float(input("Введіть h: "))
if h <=  0:
    print("Помилка: крок h  повинен бути більшим за 0")
else:
    while a < b:
        y = (a ** 3 + math.log(abs(a))) / (3 ** a)
        print("x=%i y=%.3f"%(a,y))
        a = a + h 