'''
    Cho 1 list chứa các tuple không rỗng. Viết chương trình sắp xếp list đó
    theo chiều tăng dần của phần tử cuối trong mỗi tuple.
    Ví dụ: [(2, 5), (4, 1), (0, 0)]  => [(0, 0), (4, 1), (2, 5)]
'''

# def get_last(x):
#     return x[-1]

list1 = [(2, 5), (4, 1), (0, 0), (1,9), (2,8)]
# list1.sort(key = get_last)
list1.sort(key = lambda x: x[1])

print(list1)

# list2 =[]
# list3 =[]
#
# for i in list1:
#     list2.append(i[1],)
#
# list2.sort()
# print(list2)
#
# for l in list2:
#     for q in list1:
#         if l == q[1]:
#             list3.append(q)
#
# print(list3)
