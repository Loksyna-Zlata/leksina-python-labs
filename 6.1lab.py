import math
a = int(input("Введіть a: "))
b = int(input("Введіть b: "))
h = int(input("Введіть h: "))
if h <=  0:
    print("Помилка: крок h  повинен бути більшим за 0")
else: 
    for i in range(a,b,h):
        y = (i ** 3 + math.log(abs(i))) / (3 ** i)
        print("x=%i y=%.3f"%(i,y)) 