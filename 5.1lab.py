import math
x = float(input("Введіть x: "))

if x >= 1:
    y = 7 * math.log(x) + math.log(x, 7) + math.log10(x)

elif x > -10.3:
    y = math.sin(x) - math.cos(x + 2 + math.pi / 7)

else: x <= -10.3
y = 2.24 * math.exp(0.5 * x + 0.1) * 2 ** (0.3 * x)

print("f(x) = ", y)