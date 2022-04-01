'''
    Cho list sau: ["www.hust.edu.vn", "www.wikipedia.org", "www.asp.net", "www.amazon.com"]. Viết chương trình để in ra
    hậu tố (vn, org, net, com) trong các tên miền website trong list trên.
'''

list = ["www.hust.edu.vn", "www.wikipedia.org", "www.asp.net", "www.amazon.com"]
temp_list = []
for i in list:
    post = i.split('.')[-1]
    temp_list.append(post)

post_tuple = tuple(temp_list)

print(post_tuple)