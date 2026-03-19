# Человек вводит на сайте номер телефона, ему позволено для удобства использовать кроме плюса и цифр знаки ‘-’, ‘)’, ‘(’ и пробелы.
# Уберите их из ввода.

phone = input().strip()

clean_phone = ""

for char in phone:
    if char in '0123456789+':
        clean_phone += char

print(clean_phone)