'''
Conditional statements: if, if-else, nested if-else
loop: for,while, nested loops
control loop:break,continue,pass,return
'''

# Conditional Statements - Các câu lệnh rẽ nhánh
'''  if biểu_thức_điều_kiện:
    Câu lệnh cần chạy nếu biểu_thức_điều_kiện là đúng
'''

'''
Cú pháp của if-else
    if biểu_thức_điều_kiện:
        Câu lệnh cần chạy nếu biểu_thức_điều_kiện là đúng (True)
    else:
        if biểu_thức_điều_kiện:
    Câu lệnh cần chạy nếu biểu_thức_điều_kiện là sai (False)


Cú pháp if-elif-else
    if biểu_thức_điều_kiện_01:
        Câu lệnh cần chạy nếu biểu_thức_điều_kiện_01 là đúng (True)
    elif  biểu_thức_điều_kiện_02:
        Câu lệnh cần chạy nếu biểu_thức_điều_kiện_02 là đúng (True)
    else:
        if biểu_thức_điều_kiện:
    Câu lệnh cần chạy nếu biểu_thức_điều_kiện là sai (False)
'''

'''
a = int(input('Nhập a: '))
b = int(input('Nhập b: '))

if a > 0 and b > 0:
    print(f'Tổng của 2 số là: {a + b}')
elif a < 0 and b < 0:
    print(f'Tích của 2 số là: {a * b}')
else:
    print(f'Số nhỏ hơn là {min(a,b)}')
'''
'''
else:
    if a > b:
        print(f'Số nhỏ hơn là {b}')
    else:
        print(f'Số nhỏ hơn là {a}')
'''
# print(f'Số nhỏ hơn là {b}') if a > b else print(f'Số nhỏ hơn là {a}')
# print(f'Số nhỏ hơn là {b if a > b else a}')

'''
Cú pháp cho vòng for
    for i in sequence:
        các câu lệnh sẽ chạy của mỗi vòng lặp 
'''
# ví dụ: In ra các giá trị nguyên từ 0 đến 9

'''for i in range(10):
    if i % 2 == 0:
        print(i)
'''

'''
    không cần xuống dòng (trên cùng 1 dòng)
    print(, end= " ")
    print(*args, sep=' ', end='\n', file=None)
        *args: Cho phép in nhiều giá trị cùng lúc
        sep: Kí tự dùng để phân tách 
        end: Kí tự kết thúc sau khi in xong tất cả các giá trị. Mặc định là xuống dòng
'''
'''
a = int(input('Nhập a: '))
b = int(input('Nhập b: '))

for i in range(a + 1, b):
    print(i, end = ' ')
'''
# sai vì chưa biết a hay b lớn hơn
a = int(input('Nhập a: '))
b = int(input('Nhập b: '))

if a < b:
    for i in range(a + 1, b):
        print(i, end = ' ')
else:
    for i in range(b + 1, a):
        print(i, end = ' ')

# Cách hoán đổi 2 giá trị a, b
''' 
    if a > b:
    a, b = b, a # hóan đổi a, b
'''