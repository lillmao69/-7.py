def count_vowels_and_consonants(s):
    # Приводим строку к нижнему регистру для удобства
    s = s.lower()
    # Задаем набор гласных букв
    vowels = "aeiou"
    # Инициализируем счетчики для гласных и согласных букв
    vowels_count = 0
    consonants_count = 0

    # Подсчитываем количество гласных и согласных букв в строке
    for char in s:
        if char.isalpha():  # Проверяем, является ли символ буквой
            if char in vowels:  # Проверяем, является ли символ гласной буквой
                vowels_count += 1
            else:
                consonants_count += 1

    return vowels_count, consonants_count

# Запрос у пользователя ввода строки
user_input = input("Введите строку: ")

# Подсчет количества гласных и согласных букв
vowels, consonants = count_vowels_and_consonants(user_input)

# Вывод результатов
print(f"Количество гласных букв: {vowels}")
print(f"Количество согласных букв: {consonants}")
