"Viết chương trình phân tích số nguyên n thành các thừa số nguyên tố trong Python. Ví dụ: 100 = 2x2x5x5"

n = int(input('Nhập n: '))

def phantich(n):
    l = []
    i = 2
    while n > 1:
        if n % i == 0:
            n = int(n / i)
            l.append(i)
        else:
            i += 1
    if len(l) == 0:
        l.append(n)
    return l

sb = ''
listnumber = phantich(n)
for i in listnumber:
    sb = sb + str(i) + 'x'

kq = sb[:-1]
print(listnumber)
print(f'{n} = {kq}')