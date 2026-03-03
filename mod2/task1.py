# Найдите остаток при делении числа a на b.

input_str = input().strip()

a = ''
b = ''
is_a = True

for char in input_str:
    if char == ',':
        is_a = False
        continue
    if char == ' ':
        continue
    if is_a:
        a += char
    else:
        b += char

remainder = int(a) % int(b)
print(remainder)