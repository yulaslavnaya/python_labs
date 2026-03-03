# На вход подается последовательность целых чисел.
# Требуется определить, присутствуют ли в этой последовательности одинаковые числа. Результат вернуть в формате Boolean.
numbers_input = input().split()

numbers = list(map(int, numbers_input))

print(len(numbers) != len(set(numbers)))
