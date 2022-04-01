"Viết chương trình kiểm tra một số n là số thuận nghịch trong Python. Số nguyên dương n được nhập từ bàn phím"

n = int(input('Nhập n: '))

def check(n):
    sb = str(n)
    sb1 = sb[::-1]
    if sb == sb1:
        return True
    else:
        return False

print(check(n))

