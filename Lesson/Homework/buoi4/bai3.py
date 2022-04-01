s = input('Nhập chuỗi s: ')
max_s = s[0]
min_s = s[0]
for i in range(len(s)):
    if max_s < s[i]:
        max_s = s[i]

for j in range(len(s)):
    if s[j] < min_s:
        min_s = s[j]

print(f'Ký tự lớn nhất và nhỏ nhất là: {max_s}, {min_s}')
