# На вход подается список чисел через пробел. Напишите функцию выводящую сообщение для списка чисел:
# 1) Все числа равны
# 2) Все числа разные
# 3) Есть равные и неравные числа

def analyze_numbers(numbers_str):
    numbers = list(map(int, numbers_str.split()))

    first_number = numbers[0]
    all_equal = True

    # Проверяем, все ли числа равны
    for num in numbers[1:]:
        if num != first_number:
            all_equal = False
            break

    if all_equal:
        print("Все числа равны")
        return

    # Проверяем, все ли числа разные
    # Для этого создадим множество и сравним его размер с длиной списка
    unique_numbers = set(numbers)
    if len(unique_numbers) == len(numbers):
        print("Все числа разные")
    else:
        print("Есть равные и неравные числа")



if __name__ == "__main__":
    input_string = input("Введите числа через пробел: ").strip()

    analyze_numbers(input_string)

