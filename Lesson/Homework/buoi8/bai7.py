'''
Viết hàm đếm số lần xuất hiện các ký tự trong một String
Ví dụ:
Input: ‘Stringings’
Output: {‘S’: 1, ‘t’: 1, ‘r’: 1, ’i’: 2, ‘n’: 2, ‘g’: 2, ‘s’: 1}
'''

my_string = 'Consequence'
so_lan_xuat_hien = {}

for i in my_string:
    if i in so_lan_xuat_hien:
        so_lan_xuat_hien[i] += 1
    else:
        so_lan_xuat_hien[i] = 1

print(f'Số lần xuất hiện các ký tự trong chuỗi "{my_string}" là: ')
print(so_lan_xuat_hien)