import csv
a = input("Введіть слово: ")

f = open('paper.txt', 'r')
text = f.read()
f.close()

frequency = {}

for i in a:
    if i not in frequency:
        n = 0
        for j in text:
            if j == i:
                n = n + 1
        frequency[i] = n

f = open('frequency.csv', 'w', newline='')
writer = csv.writer(f)

writer.writerow(['Letter', 'Count'])

for i in frequency:
    writer.writerow([i, frequency[i]])

f.close()

print("Дані записано у файл frequency.csv")