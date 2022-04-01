"""
Viết hàm
        def change_upper_lower(str)
    chuyển toàn bộ các ký tự in hoa sang in thường và in thường thành in hoa trong str
"""


def change_upper_lower(str):
    chuoimoi = ""
    for i in range(0, len(str)):
        if str[i].isupper():
            chuoimoi += str[i].lower()
        else:
            chuoimoi += str[i].upper()
    return chuoimoi


print(change_upper_lower('ABcd'))
