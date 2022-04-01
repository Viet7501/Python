n = int(input('Nhập độ dài list: '))
s = []

for i in range(n):
    s.append(int(input(f's[{i}]: ')))

max = s[0]
min = s[0]
for i in s:
    if i < min:
        min = i
    if i > max:
        max = i

print(f'Số lớn nhất và nhỏ nhất trong {s} là: {max}, {min}')