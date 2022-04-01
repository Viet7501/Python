"""Viết chương trình liệt kê các số
Fibonacci nhỏ hơn n là số nguyên tố trong Python. N là số nguyên dương được nhập từ bàn phím"""


def fibo(n):
    if n == 1 or n == 2:
        return 1
    elif n == 0:
        return 0
    else:
        return fibo(n - 1) + fibo(n - 2)


def nguyento(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


n = int(input("Nhập n: "))
listFibo = []
for i in range(0, n):
    listFibo.append(fibo(i))

sb = ''
for j in listFibo:
    if nguyento(j):
        sb = sb + str(j) + ' '

print(listFibo)
print(sb)