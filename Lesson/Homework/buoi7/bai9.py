'''
    Viết chương trình tính tổng và tìm giá trị lớn nhất
    trong tuple chứa các số thực.
'''

my_tuple = (1.0, 2.5, 1.667, 3.99, 5.5, 4.5, 10.0, 200.1)
max = my_tuple[0]

for i in my_tuple:
    if i >= max:
        max = i
print(f'Tổng của tuple chứa các số thực = {sum(my_tuple)}')
print(f'Giá trị lớn nhất của tuple chứa các số thực là {max}')
