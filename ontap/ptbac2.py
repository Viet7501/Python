"Viết chương trình Python giải phương trình bậc 2: ax2 + bx + c = 0."
import math

a = float(input('Nhập a: '))
b = float(input('Nhập b: '))
c = float(input('Nhập c: '))


def ptbac2(a, b, c):
    # kiểm tra các hệ số
    if a == 0:
        if b == 0:
            if c == 0:
                print('Phương trình vô số nghiệm')
            else:
                print('Phương trình vô nghiệm')
        else:
            print(f'Phương trình có một nghiệm x = {-c / b}')

    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print('Phương trình vô nghiệm')
    elif delta == 0:
        print(f'Phương trình có nghiệm kép x = {-b / 2 * c, 3}')
    else:
        print("Phương trình có 2 nghiệm phân biệt")
        print(f'x1 = {round((-b - math.sqrt(delta)) / (2 * a), 3)}')
        print(f'x2 = {round((-b + math.sqrt(delta)) / (2 * a), 3)}')


pt = ptbac2(a, b, c)
