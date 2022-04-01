'''
Viết chương trình tính tích value của các phần tử trong một dict
'''

my_dict = {
    1: 1,
    2: 2,
    5: 3,
    9: 19,
    10: 201,
    20: 99
}
tich = 1

for i in my_dict:
 tich *= my_dict[i]

print(f'Tích value của các phần tử trong dict là: {tich}')