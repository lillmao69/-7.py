# Запрос у пользователя ввода числа, для которого нужно вывести таблицу умножения
number = int(input("Введите число: "))

# Вывод таблицы умножения
print(f"Таблица умножения для числа {number}:")
for i in range(1, 11):
    result = number * i
    print(f"{number} * {i} = {result}")