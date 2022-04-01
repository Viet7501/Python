"""
Viết hàm
        def count_upper_lower(str)
    trả lại số lượng chữ cái viết hoa, số lượng chữ cái viết thường trong chuỗi str
"""

def count_upper_lower(str):
    upper = 0
    lower = 0
    for i in str:
        if 'a' <= i <= 'z':
            lower += 1
        elif 'A' <= i <= 'Z':
            upper += 1
    return upper, lower


print(count_upper_lower('ABcd'))
print(count_upper_lower('Python 3'))

