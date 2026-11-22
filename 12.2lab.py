import random

def generate_number():
    number = ""

    for i in range(7):
        number = number + str(random.randint(0, 9))

    y = random.randint(2000, 2022)

    number = number + "-" + str(y)
    return number 

n = int(input("Введіть кількість номерів: "))

numbers = []

for i in range(n):
    number = generate_number()
    numbers.append(number)

f = open("engines.txt", "w")

for number in numbers:
    f.write(number + "\n")

f.close()

uniq_numbers = set(numbers)
print("Кількість унікальних номерів:", len(uniq_numbers))