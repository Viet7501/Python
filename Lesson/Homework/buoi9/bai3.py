"""
def is_perfect(n)
    để kiểm tra xem số tự nhiên n có phải là số
    hoàn hảo hay ko, trả lại True nếu có, False nếu không.
"""

def is_perfect(n):
    tong_uoc = 0
    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i
    return True if tong_uoc == n else False


n = 8128
print(f'{n} là số hoàn hảo? {is_perfect(n)}')




# def is_perfect(n):
#     uoc = []
#     if n <= 0:
#         return 'Không phải số hoàn hảo'
#     else:
#         for i in range(1, n):
#             if n % i == 0:
#                 uoc.append(i)
#     if sum(uoc) == n:
#         return 'Số hoàn hảo'
#     else:
#         return 'Không phải số hoàn hảo'
#
#
# print(is_perfect(6))
# print(is_perfect(10))
# print(is_perfect(28))
# print(is_perfect(100))
# print(is_perfect(-5))
# print(is_perfect(0))



