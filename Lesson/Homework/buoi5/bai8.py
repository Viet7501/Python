'''
    Cho list các số nguyên dương A. Xây dựng chương trình đếm
    số lượng tập gồm 2 phần tử A[i] và A[j] thỏa mãn A[i] > A[j] và i < j.
'''

n = int(input('Nhập độ dài list: '))
s = []
count = 0

while True:
    x = int(input('Nhập x: '))
    if x > 0:
        s.append(x)
    else:
        print('x không phải số nguyên dương')
    if len(s) > n-1:
        break

for j in range(len(s)):
    for i in range(j):
        if s[i] > s[j] and i < j:
            count += 1

print(count)
