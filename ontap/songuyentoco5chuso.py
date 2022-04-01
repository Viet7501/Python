"Viết chương trình liệt kê tất cả số nguyên tố có 5 chữ số trong Python"

def nguyento(n):
    if n < 2:
        return False
    for i in range (2, n):
        if n % i == 0:
            return False
    return True

sb = []
for i in range (10000, 100000):
    if nguyento(i):
        sb.append(i)

print(sb)
print(len(sb))