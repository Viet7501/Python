'''
    Viết chương trình sinh một tuple chứa các phần tử có các kiểu
    dữ liệu khác nhau. Sau đó, unpack các phần tử trong một tuple.
'''

my_tuple = (1,3+2j,'hello', [2,4,5])
a, b, c, d = my_tuple

print(a, b, c, d)
print(type(my_tuple))