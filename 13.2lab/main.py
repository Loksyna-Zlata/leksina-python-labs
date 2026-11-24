import random
from vector import VECTOR

v1 = VECTOR("Вектор 1", random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10))

v2 = VECTOR("Вектор 2", random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10))
print("Координати першого вектора:", v1.x1, v1.y1, v1.x2, v1.y2)
print("Координати другого вектора:", v2.x1, v2.y1, v2.x2, v2.y2)

v3 = v1.Plus(v2)
print("Координати суми:", v3.x1, v3.y1, v3.x2, v3.y2)

if v3.x2 < 0 and v3.y2 < 0:
    v3.ShowName()
else:
    print("Сума векторів не знаходиться в III чверті")