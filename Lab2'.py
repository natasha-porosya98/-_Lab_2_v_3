print("Завдання 1")
import random
win_human = 0
win_comp = 0
draw = 0
while True:
    print("1.Почати грати")
    print("2. Вийти")
    op = int(input("Введіть номер: "))
    if op == 2:
        break
    if op == 1:
        human = int(input("Введіть номер: 1.Камінь, 2. Ножиці, 3. Папір ")) - 1
        variant = ['камінь', 'ножиці', 'папір']
        comp = random.randint(0, 2)
        print(f"Ви обрали:{variant[human]} ")
        print(f"Комп'ютер обрав:{variant[comp]} ")
        if human == comp:
            print("Нічия")
            draw +=1
        elif human == 0 and comp == 1:
            print("Ви виграли!")
            win_human +=1
        elif human == 1 and comp == 2:
            print("Ви виграли!")
            win_human += 1
        elif human == 2 and comp == 0:
            print("Ви виграли!")
            win_human +=1
        else:
            print("Виграв комп'ютер")
            win_comp +=1
    else:
        print("Неправельний вибір!")
print(f"Ви виграли:{win_human} ")
print(f"Виграв комп'ютер:{win_comp} ")
print(f"Нічия:{draw} ")

print("2 завдання")
n = 0
while not n:
    n = int(input("Введіть розмір списку: "))
list_number = [random.randint(1,100) for _ in range(n)]
average = sum(list_number) // n
bigger = []
for number in list_number:
    if number>average:
        bigger.append(number)

print(f"Список: {list}")
print(f"Середнє арифметичне: {average}")
print(f"Числа, що більше за середнє арифметичне: {bigger}")

print("3 завдання")
text = ""
while not text  :
    text = input("Введіть текст англійською(не порожній): ")
vowels = "AEIOUaeiou"
modified_text = ''.join(['#' if char in vowels else char for char in text])
print(f"Змінений текст: {modified_text}")

print("4 завдання")
n = int(input("Введіть розмір матриці (n): "))
data = input(f"Введіть {n * n} цілих чисел для матриці {n}x{n}, розділених пробілом: ").split()
while len(data) != n * n:
    data = input(f"Помилка: потрібно ввести рівно {n * n} чисел.")
matrix = []
for i in range(n):
   row = list(map(int, data[i * n:(i + 1) * n]))
   matrix.append(row)
print("Матриця:")
for row in matrix:
    print(row)
symmetric = True
for i in range(n):
    for j in range(i + 1, n):
        if matrix[i][j] != matrix[j][i]:
            symmetric = False
            break
    if not symmetric:
        break
if symmetric:
    print("Матриця симетрична відносно головної діагоналі.")
else:
    print("Матриця не симетрична відносно головної діагоналі.")
