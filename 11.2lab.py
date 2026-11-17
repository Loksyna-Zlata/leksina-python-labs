import json
n = int(input("Введіть кількість студентів: "))

students = {}

for i in range(n):
    surname = input("Введіть прізвище студента: ")
    grade = int(input("Введіть оцінку: "))
    students[surname] = grade

f = open('students.txt', 'w', encoding='utf-8')
json.dump(students, f, ensure_ascii=False)
f.close()

f = open('students.txt', 'r', encoding='utf-8')
students = json.load(f)
f.close()

student_list = []

for surname in students:
    student_list.append([surname, students[surname]])

for i in range(len(student_list)):
    for j in range(i + 1, len(student_list)):
        if student_list[i][1] < student_list[j][1]:
            student_list[i], student_list[j] = student_list[j], student_list[i]

k = int(len(student_list) * 0.4)

print("Студенти, які можуть претендувати на стипендію: ")

for i in range(k):
    print(student_list[i][0], student_list[i][1])