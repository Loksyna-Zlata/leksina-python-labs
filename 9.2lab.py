K = set(range(1, 51))
M = set()

for i in K:
    if i > 1:
        M.add(i - 1)

print("Множина M: ", M)