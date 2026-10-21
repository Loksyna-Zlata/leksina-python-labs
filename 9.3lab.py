a = int(input("Введіть кількість сайтів: "))
sites = dict()
description = dict()

for i in range(1, a + 1):
    sites[i] = input("Введіть адресу сайта: ")
    description[i] = input("Введіть опис сайта: ")

print("Адреси сайтів та їх описи: ")

for i in sites:
    print(sites[i], "-", description[i])