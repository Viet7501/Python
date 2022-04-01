"""
Viết chương trình tính tổng của các chữ số của môt số nguyên n trong Python
. Số nguyên dương n được nhập từ bàn phím. Với n = 1234, tổng các chữ số: 1 + 2 + 3 + 4 = 10
"""

import math


def tong(n):

    listnumbers = []
    while n > 0:
        listnumbers.append(n % 10)
        n = n // 10
    return listnumbers


n = int(input('Nhập n: '))
tong = tong(n)
ans = 0
sb = ''
for i in tong:
    sb = sb + str(i) + '+'
    ans += i

kq = sb[-2::-1]
print(f'{kq} = {ans}')