# Для введенного в десятичном коде натурального числа найти представление в двоичном, восьмеричном и шестнадцатеричном кодах.
# Если введено не натуральное число, вывести диагностику: «Неверный ввод».
# Использовать встроенные возможности языка python запрещено.

input_str = input().strip()

is_valid = True
for char in input_str:
    if char < '0' or char > '9':
        is_valid = False
        break

if is_valid:
    number = 0
    for char in input_str:
        number = number * 10 + (ord(char) - ord('0'))

    if number <= 0:
        print("Неверный ввод")
    else:
        # Двоичная система
        n = number
        binary = ""
        while n > 0:
            binary = chr(ord('0') + (n % 2)) + binary
            n = n // 2

        # Восьмеричная система
        n = number
        octal = ""
        while n > 0:
            octal = chr(ord('0') + (n % 8)) + octal
            n = n // 8

        # Шестнадцатеричная система
        n = number
        hex_value = ""
        while n > 0:
            remainder = n % 16
            if remainder < 10:
                hex_value = chr(ord('0') + remainder) + hex_value
            else:
                hex_value = chr(ord('A') + remainder - 10) + hex_value
            n = n // 16

        print(f"{binary}, {octal}, {hex_value}")
else:
    print("Неверный ввод")