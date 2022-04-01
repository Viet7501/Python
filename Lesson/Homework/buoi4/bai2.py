s = input('Nhập chuỗi s: ')

if len(s) < 2:
    print('')
else:
    print(s[0] + s[1] + s[-2] + s[-1])