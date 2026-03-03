# На вход подается строка s и символ i. Необходимо найти количество символов i, расположенных в начале строки.
input_str = input().strip()

s = ''
i = ''
is_s = True

for char in input_str:
    if char == ',':
        is_s = False
        continue
    if char == ' ':
        continue
    if is_s:
        s += char
    else:
        i += char

count = 0
for char in s:
    if char == i:
        count += 1
    else:
        break

print(count)