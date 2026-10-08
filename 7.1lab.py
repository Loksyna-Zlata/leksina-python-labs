text = input("Введіть слова через пробіл: ")
spysok = text.split(" ")

len_spysok = len(spysok)
max_count = 0
max_word = ""

for i in range(len_spysok):
    count = spysok[i].count("а")
    if count > max_count:
        max_count = count 
        max_word = spysok[i]
    elif count == max_count:
        max_word = max_word + ", " + spysok[i]
if max_word != "":
    print("Слова, що містять найбільшу к-сть літер (а): ", max_word)
else:
    print("В жодному слові немає літери (а)")