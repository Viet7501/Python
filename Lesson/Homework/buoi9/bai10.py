"""
Cho dãy số Tribonacci với công thức truy hồi sau:
            F(n) = F(n-1) + F(n-2) + F(n-3),    F(1) = 1, F(2) = 1, F(3) = 2
    Xây dựng 2 hàm để tìm ra số thứ n trong dãy số theo:
        + Hàm Đệ quy
        + Hàm Không đệ quy
"""


def tribonacci(n):
    if 0 <= n <= 2:
        return 1
    elif n == 3:
        return 2
    else:
        return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)

while True:
    n = int(input('Nhập n: '))
    if n > 0:
        break
    print('Phải nhập số nguyên dương')

print(f'Số thứ {n} trong dãy só Tribonacci là: {tribonacci(n)}')

def tribo(n) :
    if (n < 1) :
        return

    trib_0 = 1
    trib_1 = 1
    trib_2 = 2
    trib_n = trib_0 + trib_1 + trib_2


    for i in range(3, n) :
        trib_n = trib_0 + trib_1 + trib_2
        trib_0 = trib_1
        trib_1 = trib_2
        trib_2 = trib_n

    return trib_n


print(f'Số thứ {n} trong dãy só Tribonacci là: {tribo(n)}')
