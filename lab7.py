import math
a = float(input("Введіть початкове значення a: "))
b = float(input("Введіть кінцеве значення b: "))
h = float(input("Введіть крок h: "))
for x in range(int(a * 1000), int(b * 1000), int(h * 1000)):
    x /= 1000
    f_x = x * math.sin(math.sin(x)) + math.cos(math.cos(x))
    print(f"f({x}) = {f_x}")
