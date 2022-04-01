'''
    Nhập vào số tự nhiên x, tìm số n lớn nhất mà tổng các
    số tự nhiên đến n không vượt quá x
'''
x = int(input('Nhập x: '))
n = 1
tong = 0
while x >= 0:
    x = x - n
    n += 1
print(n - 2)


while True:
    if tong + n < x:
        tong += n
        n += 1
    else:
        break
print(n - 1)