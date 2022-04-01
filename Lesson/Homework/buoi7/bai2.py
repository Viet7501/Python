'Viết chương trình đảo ngược một tuple.'

my_tuple = (1,2,3,4)
list = list(reversed(my_tuple))
reversed_tuple = tuple(list)

print(reversed_tuple)
print(type(reversed_tuple))