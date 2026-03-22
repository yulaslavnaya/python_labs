# Дано количество имён N. Вводится N имен и помещаются в список. Создайте новый список uni:
# - Пройдите по исходному списку names и добавьте имя в uni только в том случае, если имени с такой длиной в uni ещё нет. В итоге в uni должны быть имена разной длины.
# - Выведите оба списка.

N = int(input("Введите количество имён: "))

names = []

# Вводим N имён
for i in range(N):
    name = input(f"Введите имя {i + 1}: ")
    names.append(name)

uni = []

for name in names:
    # Проверяем, есть ли в uni имя с такой же длиной
    name_length = len(name)
    has_same_length = False

    for existing_name in uni:
        if len(existing_name) == name_length:
            has_same_length = True
            break

    # Если имени с такой длиной ещё нет, добавляем
    if not has_same_length:
        uni.append(name)

print("\nИсходный список имён:", names)
print("Список имён разной длины:", uni)