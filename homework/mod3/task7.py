# Человек вводит на сайте номер телефона, ему позволено для удобства использовать кроме плюса и цифр знаки ‘-’, ‘)’, ‘(’ и пробелы.
# Уберите их из ввода.
phone = input()

digits_and_plus = [c for c in phone if c.isdigit() or c == '+']

print(''.join(digits_and_plus))