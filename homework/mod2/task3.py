# Рассмотрим три числа a, b и c. Упорядочим их по возрастанию. Какое число будет стоять между двумя другими?

# Чтение входных данных
input_str = input().strip()

# Поиск первого пробела
first_space = -1
for i in range(len(input_str)):
    if input_str[i] == ' ':
        first_space = i
        break

# Поиск второго пробела
second_space = -1
for i in range(first_space + 1, len(input_str)):
    if input_str[i] == ' ':
        second_space = i
        break

# Извлечение чисел
a = int(input_str[:first_space])
b = int(input_str[first_space + 1:second_space])
c = int(input_str[second_space + 1:])

# Поиск среднего числа
if (b <= a <= c) or (c <= a <= b):
    middle = a
elif (a <= b <= c) or (c <= b <= a):
    middle = b
else:
    middle = c

print(middle)