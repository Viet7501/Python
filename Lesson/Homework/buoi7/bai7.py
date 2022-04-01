'Viết chương trình kiểm tra 2 tuple có phần tử chung hay không.'


tuple_1 = (1, 2, 3, 4, 9, 10, True, 'v')
tuple_2 = (1, 3, True, False, 'v', 'Hello')
set1 = set(tuple_1)
set2 = set(tuple_2)


if len(set1.intersection(set2)) > 0:
    print('2 tuple có phần tử chung')
else:
    print('2 tuple không có phần tử chung')






# count = 0
#
# for i in tuple_1:
#     if i in tuple_2:
#         count += 1
#
#
# print(count)