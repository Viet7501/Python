'''
    Viết chương trình kiểm tra xem tất cả các phần tử trong
    tuple có giống nhau hay không.
'''

my_tuple = (1, 2, 3, 4, 5, 6, 'v')
our_tuple = (1, 1, 1, 1, 1, 1, 1)

my_set = set(my_tuple)
our_set = set(our_tuple)

if len(my_set) == 1:
    print('Các phần tử trong tuple có giống nhau')
else:
    print('Các phần tử trong tuple không giống nhau')

if len(our_set) == 1:
    print('Các phần tử trong tuple có giống nhau')
else:
    print('Các phần tử trong tuple không giống nhau')