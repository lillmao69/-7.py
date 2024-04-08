# Запрос у пользователя ввода целого числа больше 1
number = int(input("Введите целое число больше 1: "))

# Проверка числа на простоту
if number <= 1:
    print("Число должно быть больше 1.")
else:
    is_prime = True
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

    # Вывод результата
    if is_prime:
        print(f"{number} - простое число.")
    else:
        print(f"{number} - составное число.")
