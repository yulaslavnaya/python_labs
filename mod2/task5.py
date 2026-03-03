# На вход подается доменное имя сайта. Необходимо вывести все домены по порядку начиная с домена первого уровня.
domain = input().strip()

parts = []
current = ""

for ch in domain:
    if ch == '.':
        parts.append(current)
        current = ""
    else:
        current += ch
parts.append(current)

i = len(parts) - 1
while i >= 0:
    print(parts[i])
    i -= 1