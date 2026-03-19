# Дан список слов. Составить из последних букв каждого слова новое.
words_line = input().strip()

new_word = ""
current_word = ""

for char in words_line:
    if char == ' ':
        if current_word:
            new_word += current_word[-1]
            current_word = ""
    else:
        current_word += char

if current_word:
    new_word += current_word[-1]

print(new_word)