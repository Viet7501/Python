"Viết chương trình liệt kê n số nguyên tố đầu tiên trong Python. Số nguyên dương n được nhập từ bàn phím"

n = int(input('Nhập n: '))

def nguyento(n):
    if n < 2:
        return False
    for i in range (2, n):
        if n % i == 0:
            return False
    return True

dem = 0 # đếm số số nguyên tố
i = 2  # tìm số nguyên tố bắt dầu từ số 2
sb = ""
while (dem < n):
    if (nguyento(i)):
        sb = sb + str(i) + " "
        dem = dem + 1
    i = i + 1
print(sb)