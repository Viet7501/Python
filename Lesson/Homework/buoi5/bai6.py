'''
    Viết chương trình đếm các chuỗi trong một list thỏa mãn:
        + Độ dài từ 2 trở lên
        + Ký tự đầu tiên và cuối cùng của chuỗi đó giống nhau
'''

n = int(input('Nhập độ dài list: '))
s = []

for i in range(n):
    s.append((input(f's[{i}]: ')))

count = 0
for i in s:
 if len(i) >= 2 and i[0] == i[-1]:
        count += 1

print(f'Số chuỗi trong list thỏa mãn yêu cầu là: {count}')
