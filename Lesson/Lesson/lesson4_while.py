# Cú pháp cho vòng while
'''
    while biểu_thức_điều_kiện:
        Các câu lệnh sẽ chạy của mỗi vòng while,một vòng while được chạy khi biểu_thức_điều_kiện là Đúng (True)
'''
'''
while True: #tạo vòng lặp vô hạn
    n = int (input('Nhập n = '))
    if n > 0:
        print('Đã nhập số dương. Chương trình đã dừng lại!')
        break
    print('Đã nhập số không dương. Chương trình sẽ tiếp tục!')
'''

""" 
Cú pháp cho vòng while
    while biểu_thức_điều_kiện:
        các câu lệnh sẽ chạy của mỗi vòng while, một vòng while được chạy khi biểu_thức_điều_kiện là Đúng (True)
"""

# Nhập vào một số tự nhiên n rồi tính tổng các số tự nhiên đến n
n = int(input("Nhập n = "))
i = 0
sum_n = 0
while i <= n:
    sum_n = sum_n + i
    i += 1  # tăng biến đếm lên 1
print(f"Tổng các số tự nhiên đến {n} là: {sum_n}")

# Nhập vào một số tự nhiên x, tìm số n lớn nhất mà tổng các số tự nhiên đến n không vượt quá x
x = int(input("Nhập x = "))
n = 0
sum_n = 0
while sum_n <= x:
    n += 1
    sum_n = sum_n + n

print(f"Số n lớn nhất là {n-1}")

""" Lập chương trình thực hiện các công việc sau:
    + Nhập số epsilon < 1  từ bàn phím
    + Tính e = 1+\dfrac{1}{1!} + \dfrac{1}{2!} + ... +\dfrac{1}{n!} quá trình dừng khi \dfrac{1}{n!} <  epsilon.
    + Đưa kết quả ra màn hình
"""
epsilon = float(input("Nhập epsilon = "))
fact_max = 1/epsilon  # Đổi lại điều kiện dừng lặp
i = 1
factorial = 1
value_e = 1
while factorial <= fact_max:
    value_e += 1 / factorial
    i += 1
    factorial *= i
print('Giá trị của e ~ ', value_e)

""" Nested while và Nested for-while: Giống như phần Nested for """
outer = 1
while outer < 2:
    inner = 3
    while inner < 6:
        print(outer, ':', inner)
        inner += 1
    outer += 1


""" 
    Thay đổi luồng của vòng lặp. Các câu lệnh trong vòng lặp sẽ chạy mãi cho đến khi biểu_thức_điều_kiện Sai(False).
    Trong nhiều trường hợp, cần dừng vòng lặp hiện tại hoặc dừng hoàn toàn vòng lặp.
"""

""" Cú pháp của break - dừng toàn bộ việc lặp
        for val in sequence:
            ...
            if điều_kiện:
                break
            ...
        ...
        while biểu_thức_điều_kiện_w:
            ...
            if điều_kiện:
                break
            ...
        ...
"""
# Viết chương trình kiểm tra số mà người dùng nhập vào là số dương thì dừng lại

while True:
    print("Nhập 1 số nguyên:", end=" ")
    n = int(input())
    if n > 0:
        print("Đã nhập số dương. Chương trình đã dừng lại!")
        break
    print("Đã nhập số âm. Chương trình sẽ tiếp tục!")

""" Cú pháp của continue - dừng vòng lặp hiện tại
        for val in sequence:
            ...
            if điều_kiện:
                continue
            ...
        ...
        while biểu_thức_điều_kiện_w:
            ...
            if điều_kiện:
                continue
            ...
        ...
"""

# Chương trình chỉ in ra các số có 2 chữ số và ko chia hết cho 1 trong các số 2, 3, 5
for i in range(10, 100):
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
        continue
    print(i, end=" ")


""" pass
    - Là 1 câu lệnh rỗng
    - Trình thông dịch có thông dịch qua nó nhưng sẽ ko có chuyện gì xảy ra. Khác với comment, trình thông dịch bỏ qua
    - Dùng trong khi mà chúng ta chưa nghĩ ra phần thân cho các câu lệnh if, else, for, while, ...
"""

for i in range(10):
    pass


_str = 'example-pass'
if 'a' in _str:
    pass

""" return => sẽ giới thiệu trong phần học về function """