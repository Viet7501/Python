'''
    Viết chương trình chia một list thành 2
    phần với độ dài phần đầu được nhập vào từ bàn phím.
'''

n = int(input('Nhập độ dài list: '))
s = []
s1 = []

for i in range(n):
    s.append(int(input(f's[{i}]: ')))

cut = int(input('Độ dài phần đầu: '))
s1 = s[0:cut:]
s = s[cut::]

print(s1)
print(s)