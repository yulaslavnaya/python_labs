# На вход подается два числа через пробел: a, b.
# Напишите функцию для реализации рекурсивного алгоритма Евклида поиска наибольшего общего делителя.
def gcd_recursive(a, b):
    if b == 0:
        return abs(a)

    return gcd_recursive(b, a % b)


if __name__ == "__main__":
    input_string = input("Введите два числа через пробел: ").strip()

    a_str, b_str = input_string.split()
    a = int(a_str)
    b = int(b_str)

    result = gcd_recursive(a, b)
    print(f"\nНОД({a}, {b}) = {result}")




