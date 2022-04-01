n = int(input("Nhập n: "))
x = float(input("nhập x: "))

s_1 = 1
s_2 = 1
s_3 = 1
a = 1
b = 1
c = 1

for i in range(1, n + 1):
    a = a * x
    s_1 += a

print(s_1)

for i in range(1, n + 1):
    b = b * (-x)
    s_2 += b

print(s_2)

for i in range(1, n + 1):
    c = c * (x / i)
    s_3 += c

print(s_3)
