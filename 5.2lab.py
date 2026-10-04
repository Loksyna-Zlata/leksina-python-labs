import math
print("Точка A: ")
xA = float(input("xA = "))
yA = float(input("yA = "))

print("Точка B: ")
xB = float(input("xB = "))
yB = float(input("yB = "))

print("Точка C: ")
xC = float(input("xC = "))
yC = float(input("yC = "))

dA = math.sqrt(xA ** 2 + yA ** 2)
dB = math.sqrt(xB ** 2 + yB ** 2)
dC = math.sqrt(xC ** 2 + yC ** 2)

if dA < dB and dA < dC:
    print("Найближча до центру координат точка A")
elif dB < dA and dB < dC:
    print("Найближча до центру координат точка B")
elif dC < dA and dC < dB:
    print("Найближча до центру координат точка C")
elif dA == dB and dA == dC:
    print("Всі три точки знаходяться на однаковій відстані від центру")
elif dA == dB and dA < dC:
    print("Найближчі до центру координат точки A та B")
elif dA == dC and dA < dB:
    print("Найближчі до центру координат точки A та C") 
else:
    print("Найближчі до центру координат точки B та C")