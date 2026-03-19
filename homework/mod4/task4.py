# На вход подается строка.
# Напишите функцию для реализации: если из слова можно составить палиндром, то составить его и вывести на экран.

def can_form_palindrome(s):
    # Подсчитываем частоту каждого символа
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Для палиндрома должно быть не более одного символа с нечетным количеством
    odd_count = 0
    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1

    # Палиндром можно составить, если:
    # - для четной длины: все символы имеют четное количество
    # - для нечетной длины: ровно один символ имеет нечетное количество
    return odd_count <= 1


def form_palindrome(s):
    if not s:
        return "Пустая строка"

    # Проверяем, можно ли составить палиндром
    if not can_form_palindrome(s):
        return f"Из строки '{s}' нельзя составить палиндром"

    # Подсчитываем частоту каждого символа
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Находим символ с нечетным количеством (для нечетной длины)
    middle_char = ''
    half_palindrome = []

    for char, count in char_count.items():
        if count % 2 != 0:
            # Это символ, который будет в середине
            middle_char = char
            # Используем половину от четной части
            half_palindrome.append(char * (count // 2))
        else:
            # Для символов с четным количеством берем половину
            half_palindrome.append(char * (count // 2))

    # Склеиваем половину палиндрома
    half = ''.join(half_palindrome)

    # Формируем полный палиндром: половина + середина + перевернутая половина
    result = half + middle_char + half[::-1]

    return result


if __name__ == "__main__":
    input_string = input("Введите строку: ").strip()

    # Составляем палиндром (обычная версия)
    result = form_palindrome(input_string)
    print(f"\nРезультат: {result}")
