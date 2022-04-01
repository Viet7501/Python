'''
    Viết chương trình kiểm tra 2
    list có phần tử chung hay không
'''
list1 = []
list2 = []
result = 0
n = int(input('Nhập độ dài list 1: '))
print("Nhập list 1")

for i in range(n):
    list1.append((input(f's[{i}]: ')))

m = int(input('Nhập độ dài list 2: '))
print("Nhập list 2")
for i in range(m):
    list2.append((input(f's[{i}]: ')))

for i in list1:
    for j in list2:
        if i == j:
            result += 1
if result == 0:
    print('2 list không có phần tử chung')
else:
    print('2 list có phần tử chung')


