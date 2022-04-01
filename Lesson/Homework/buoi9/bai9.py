"""
Viết hàm đệ quy đếm và trả về số lượng chữ số lẻ của số nguyên dương n cho trước.
Ví dụ: Hàm trả về 4 nếu n là 19922610 (do n có 4 số lẻ là 1, 9, 9, 1)
"""


def demsole(n):

    if n == 0:
        return 0
    else:
        if n % 2 != 0:
            return 1 + demsole(n // 10)
        return demsole(n // 10)


print(demsole(1235))
print(demsole(19922610))