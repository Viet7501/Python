while True:
    n = int(input('Nhập n: '))
    if n < 1000:
        break
    print("Nhập không đúng yêu cầu bài toán, vui lòng nhập lại")
tong = 0
while n > 0:
    m = n % 10
    tong += m
    n = n // 10

print(f'Tổng các chữ số là: {tong}')
