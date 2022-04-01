s = str(input('Nhập s: '))
so = ' '

for i in s:
    if '0' < i < '9':
        so += i
print("Các ký tự số có trong chuỗi là: ")
print(so)