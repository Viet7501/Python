"""
Viết hàm
        def is_pangram(str, alphabet)
    đề kiểm tra xem chuỗi str có phải là Pangram không, trả lại True nếu có, False nếu không
    Ghi chú: Pangram là chuỗi chứa mỗi chữ cái trong bảng alphabet ít nhất 1 lần
"""


def is_pangram(str, alphabet):
    for i in alphabet:
        if i not in str:
            return False
    return True

def pangram(str, alphabet):
    if is_pangram(str, alphabet) != True:
        print('Không phải chuỗi Pangram')
    else:
        print('Là chuỗi Pangram')


pangram('A quick brown fox jumps over the lazy dog', 'abcdefghijklmnopqrstuvwxyz')
pangram('Hello my name is Viet', 'abcd')
