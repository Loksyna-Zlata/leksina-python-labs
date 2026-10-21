a = input("Введіть адреси сайтів через пробіл: ")
spysok = a.split()
T = tuple(spysok)

letters = "abcdefghijklmnopqrstuvwxyz"
Letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(26):
    N = 0
    for site in T:
        for l in site:
            if l == letters[i] or l == Letters[i]:
                N = N + 1
    if N > 0:
        print(letters[i], "-", N)