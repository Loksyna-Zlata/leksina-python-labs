f = open("America.txt", "r")
countries = []

for i in f:
    p = i.split("=")
    country = p[0].strip()
    population = int(p[1].strip())
    countries.append([country, population])

f.close()

max_population = countries[0][1]
max_country = countries[0][0]

for i in countries:
    if i[1] > max_population:
        max_population = i[1]
        max_country = i[0]

print("Країна з найбільшим населенням: ", max_country)
print("Населення: ", max_population)

for i in range(len(countries)):
    for j in range(i + 1, len(countries)):
        if countries[i][1] < countries[j][1]:
            countries[i], countries[j] = countries[j], countries[i]

f = open("sorted.txt", "w")

for i in countries:
    f.write(i[0] + " = " + str(i[1]) + "\n")

f.close() 