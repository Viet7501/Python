''' Viết chương trình in ra phần tử có số lần xuất hiện nhiều
     nhất trong một list. Nếu có nhiều phần tử có
    cùng số lần xuất hiện nhiều nhất thì in ra 1 trong số chúng.
'''

n = int(input('Nhập độ dài list: '))
s = []

for i in range(n):
    s.append(input(f's[{i}]: '))

list = set(s)
maxcount= 0


for i in list:
    if s.count(i) > maxcount:
        maxcount = s.count(i)
for i in list:
    if s.count(i) == maxcount:
        print(i)


