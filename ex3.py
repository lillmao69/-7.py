# Запрос у пользователя ввода целого неотрицательного числа
n = int(input("Введите целое неотрицательное число: "))

# Проверка, что число неотрицательное
if n < 0:
    print("Факториал определен только для неотрицательных чисел.")
elif n == 0:
    print("Факториал числа 0 равен 1.")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i

    # Вывод результата
    print(f"Факториал числа {n} равен {factorial}.")
