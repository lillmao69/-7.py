# Запрос у пользователя ввода трех чисел
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))

# Нахождение максимального числа с помощью условного оператора
if num1 >= num2 and num1 >= num3:
    max_num = num1
elif num2 >= num1 and num2 >= num3:
    max_num = num2
else:
    max_num = num3

# Вывод максимального числа
print("Максимальное число:", max_num)
