import numpy as np
import random 
a = int(input("Введіть a: "))
b = int(input("Введіть b: "))

K = np.zeros((4,5))

for i in range(4):
    for j in range(5):
        K[i][j] = random.randint(a,b)
print("K = ")
print(K)

B = np.zeros((2,10))

for i in range(2):
    for j in range(10):
        if j < 5:
            B[i][j] = K[i][j]
        else:
            B[i][j] = K[i + 2][j - 5]
print("B = ")
print(B)

C = np.zeros(10)

for i in range(10):
    C[i] = B[0][i] + B[1][i]
print("C = ")
print(C)