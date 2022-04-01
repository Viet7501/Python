'''
    Viết chương trình chuyển một tuple
    sang thành list và ngược lại từ list sang tuple
'''
my_tuple = ('hello', 1, 4)
my_list = list(my_tuple)
print(my_list)
print(type(my_list))

list = [1,2,3,4]
s = tuple(list)
print(s)
print(type(s))