def read_dictionary():
    dictionary = {}

    f = open("dictionary.txt", "r", encoding="utf-8")

    for i in f:
        key, value = i.strip().split(": ")
        dictionary[key] = value
    f.close()

    return dictionary

def unic_dictionary(dictionary):
    keys = list(dictionary.keys())

    f = open("keys.txt", "w", encoding="utf-8")
    for i in keys:
        f.write(i + "\n")
    f.close()

    values = set(dictionary.values())
    print("Унікальні значення: ")
    for i in values:
        print(i)

dictionary = read_dictionary()
unic_dictionary(dictionary)