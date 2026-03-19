# Рассмотрим три числа a, b и c. Упорядочим их по возрастанию. Какое число будет стоять между двумя другими?
a, b, c = map(int, input().split())

median = sorted([a, b, c])[1]

print(median)