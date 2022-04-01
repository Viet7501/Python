"Viết chương trình liệt kê tất cả các số nguyên tố nhỏ hơn n. Số nguyên dương n được nhập từ bàn phím"

n = int(input('Nhập n: '))

def nguyento(n):
    if n < 2:
        return False
    for i in range (2, n):
        if n % i == 0:
            return False
    return True

print ("Tất cả các số nguyên tố nhỏ hơn", n, "là:")
sb = ""

for i in range (2, n+1):
    if nguyento(i):
        sb = sb + str(i) + " "

print(sb)
