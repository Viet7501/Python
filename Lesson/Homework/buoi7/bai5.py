'''
    Viết chương trình tìm ra tuple có phần tử thứ 2
    là nhỏ nhất từ một list chứa các tuple.
'''

list1 = [(1, 2), (1, 3, 9), (1, 7), (4, 2)]
list2 = []
min = []

for i in list1:
    list2.append(i[1])

list2.sort()
print(list2)

for j in list1:
    if j[1] == list2[0]:
        print(j)
