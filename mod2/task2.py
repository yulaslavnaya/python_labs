# На вход подается длина стороны квадрата, рассчитать периметр, площадь и диагональ с округлением до 2 знака.

a = int(input().strip())

perimeter = 4 * a
area = a * a
diagonal = a * 2**0.5

print(f"{perimeter:.2f}, {area:.2f}, {diagonal:.2f}")