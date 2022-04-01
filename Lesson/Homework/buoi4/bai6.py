s = input('Nhập chuỗi: ')
k = input('Nhập ký tự: ')
count = 0

print(f'Vị trí của ký tự "{k}" trong chuỗi "{s}" là: ')
for i in range(0,len(s)):
    if k == s[i]:
        print(i, end=' ')
        count += 1

if count == 1:
    print(f'ký tự {k} không có trong chuỗi s')