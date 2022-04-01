'Viết chương trình tìm từ dài nhất trong một câu nhập vào từ bàn phím.'

s = input('Nhập câu: ')

list = list(s.split())
max = list[0]

for i in list:
    if len(i) > len(max):
        max = i

print(f'Từ dài nhất trong câu "{s} là: {max}"')


