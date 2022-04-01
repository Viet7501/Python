a = float(input('Nhập a: '))
b = float(input('Nhập b: '))
c = float(input('Nhập c: '))

if a + b <= c or b + c <= a or c + a <= b:
    print(f"Ba số {a, b, c} Không phải là độ dài các cạnh của một tam giác.")
else:
    if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
        print(f"Ba số {a, b, c} là độ dài các cạnh của một tam giác vuông.")
    else:
        print(f"Ba số {a, b, c} là độ dài các cạnh của một tam giác.")