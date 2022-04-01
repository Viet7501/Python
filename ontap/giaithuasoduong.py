while True:
    n = int(input('Nhập n: '))
    if n >= 0:
        break

def giaithua(n):
    if n == 0:
        return 1
    else:
        return n * giaithua(n-1)

print(giaithua(n))