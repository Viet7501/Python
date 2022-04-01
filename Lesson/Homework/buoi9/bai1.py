"""
    Viết hàm
        def max_min(*numbers)
trả lại cả giá trị max, min của nhiều số được truyền vào
"""


def max_min(*numbers):
    max_number = number[0]
    min_number = number[0]
    for number in numbers:
        if number >= max_number:
            max_number = number
        if number <= min_number:
            min_number = number

    return max_number, min_number


x = max_min(1, -5, 5, 75, 2.5)
print(x)