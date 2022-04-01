' Viết chương trình lấy ra các phần tử key-value xuất hiện trong cả 2 dict'

our_dict = {
    5: -5,
    3: -3,
    99: 127,
    201: 202,
    123: 134
}

my_dict = {
    1: -1,
    2: -2,
    3: -3,
    4: -4,
    5: -5,
    99: 127
}
print('Các phần tử key-value xuất hiện ở cả 2 dict là: ')
for i in our_dict:
    for j in my_dict:
        if j == i and my_dict[j] == our_dict[i]:
            print(f'{j} : {my_dict[j]}')