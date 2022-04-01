"""
Viết hàm
        def reverse_string(str)
    trả lại chuỗi đảo ngược của chuỗi str
"""


def reverse_string(str):
    string = str[::-1]
    return string


x = reverse_string('hello')
print(x)

y = reverse_string('abcdefgh')
print(y)
