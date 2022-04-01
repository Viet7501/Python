n = int(input('Nhập độ dài list: '))
s = []

for i in range(n):
    s.append(int(input(f's[{i}]: ')))

tong = 0
tich = 1

for i in s:
    tong += i
    tich *= i

print(f'Tổng các phần tử trong list là: {tong}')
print(f'Tích các phần tử trong list là: {tich}')

