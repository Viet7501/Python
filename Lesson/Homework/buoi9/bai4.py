"""
Dùng hàm is_prime(n) đã có trong bài học để xây dựng đoạn chương trình:
    1. Nhập vào số nguyên dương n từ bàn phím
    2. Tìm và in ra số nguyên tố bé nhất và lớn hơn n
"""


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def next_prime(n):
    while True:
        n += 1
        if is_prime(n):
            return n


n = 5
print(f'Số nguyên tố bé nhất và > {n} là: {next_prime(n)}')




# def is_prime(n):
#     """
#         Kiểm tra số n có phải số nguyên tố không?
#     return True nếu là số nguyên tố
#     return False nếu không là số nguyên tố
#     """
#     if n <= 1:
#         return False
#     count = 0
#     for i in range(1, n + 1):
#         if n % i == 0:
#             count += 1
#     if count == 2:
#         return True
#     else:
#         return False
#
# def in_so_nguyen_to(n):
#     so_nguyen_to = []
#     for i in range(n + 1, 2*n):
#         if is_prime(i):
#             so_nguyen_to.append(i)
#     if len(so_nguyen_to) == 0:
#         print('Số nhập không phải số nguyên dương')
#     else:
#         print(f'Số nguyên tố bé nhất lớn hơn {n}: {min(so_nguyen_to)}')
#
#
# n = int(input('Nhập n: '))
# in_so_nguyen_to(n)
