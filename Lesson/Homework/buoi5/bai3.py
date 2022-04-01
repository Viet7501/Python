'Viết chương trình tạo ra list mới bằng cách ghép một chuỗi s vào các phần tử list cũ'

n = int(input('Nhập độ dài list: '))
the_list = []
for i in range(n):
    the_list .append(input(f's[{i}]: '))

s = input("Nhập chuỗi s: ")

new_list = []
for item in the_list:
    new_list.append(s+item)
print(f'List mới: {new_list}')
