'Viết chương trình lấy ra top 3 phần tử có value lớn nhất từ dict'

my_dict = {
    -5: 1,
    99: 2,
    54: 3,
    9.77: 19,
    -100: 201,
    20: 99
}
print('Top 3 phần tử có value lớn nhất từ dict:')
sorted_Top3 = sorted(my_dict, key=my_dict.get, reverse=True)[:3]
for i in sorted_Top3:
    for j in my_dict:
        if j == i:
            print(f'{j}: {my_dict[j]}')
