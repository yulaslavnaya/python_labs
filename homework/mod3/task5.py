# Дан список слов. Составить из последних букв каждого слова новое.
words = input().split()

last_letters = [word[-1] for word in words]

print(''.join(last_letters))