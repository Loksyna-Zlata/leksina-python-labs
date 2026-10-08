z = 3
spysok = []
for i in range(z):
    y = input("Введіть слово: ")
    spysok.append(y)
max_len = 0
for y in spysok:
    if len(y) > max_len:
        max_len = len(y)
for y in spysok:
    print(y.rjust(max_len, "&"))