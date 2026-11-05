import os

print("Операційна система: ", os.name)

files = os.listdir()

print("Список файлів поточного каталогу: ")
for file in files:
    print(file)

print("Список файлів з розширенням .txt: ")
for file in files:
    if file.endswith(".txt"):
        print(file)