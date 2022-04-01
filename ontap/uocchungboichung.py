"""
Viết chương trình tìm ước số chung lớn nhất (USCLN) và bội số chung nhỏ nhất
 (BSCNN) của hai số nguyên dương a và b nhập từ bàn phím.
"""

while True:
    a = int(input('Nhập a: '))
    b = int(input('Nhập b: '))
    if a > 0 and b > 0:
        break
    else:
        print('Không phải số nguyên dương! Vui lòng nhập lại')

def uscln(a, b):
    if b == 0:
        return a
    return uscln(b, a % b)

def bcnn(a, b):
    return int(a*b/uscln(a, b))


print(uscln(a, b))
print(bcnn(a, b))