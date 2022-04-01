'''
Viết chương trình tìm giá trị lớn nhất và giá trị nhỏ nhất trong các value của dict
'''

my_dict = {
    'hello': 1,
    2: 2,
    5: 3,
    9: 19,
    10: 201,
    20: 99
}

max = my_dict[2]
min = my_dict[2]

for  i in my_dict:
    if my_dict[i] > max:
        max = my_dict[i]
    if my_dict[i] < min:
        min = my_dict[i]

print(f'Giá lớn nhất trong các value: {max}')
print(f'Giá trị nhỏ nhất trong các value: {min}')