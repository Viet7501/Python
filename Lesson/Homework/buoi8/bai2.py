'Viết chương trình tìm ra top 3 phần tử của dict có key lớn nhất'
my_dict = {
    -5: 1,
    99: 2,
    54: 3,
    9.77: 19,
    -100: 201,
    20: 99
}
print('Top 3 phần tử của dict có key lớn nhất là: ')
my_keys = sorted(list(my_dict.keys()),reverse = True)[:3]
for j in my_keys:
    for i in my_dict:
        if i == j:
            print(f'{i} : {my_dict[i]}')
