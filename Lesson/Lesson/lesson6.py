'''
    List
        Tạo, truy cập
        Các toán tử cơ bản
        Hàm và phương thức hay dùng
'''


# your_list = [1, -4, 'string', 3.14, 'abc-xyz'] #list chứa hỗn hợp kiểu dữ liệu
# print(your_list)
# print(type(your_list))
#
# our_list = [0, [1, 2, 3, 0], [3, 4, 0, 1], 'string', 1, -2, ['hi', 2, 3.14]] #Nested list
# print(our_list)
# print(type(our_list))
#
# empty_list = [] #list rỗng
# print(empty_list)
#
# _empty_list = list() #list rỗng
# print(_empty_list)
#
# 'Truy cập ào list: Giống với chuỗi'
#
# my_list = ['first', 1, 2, 3, 'a',[1, 2, 4, 6]]
# l = len(my_list)
# print(l)
# print(my_list[2:5])
# print(my_list[:-3])
# print(my_list[3:])
# print(my_list[::3])
# print(my_list[::-1])

'Các phép toán với kiểu dữ liêu list'
''' 
    Khác với chuỗi thì list là kiểu có thể thay đổi được
'''

# phép toán gán (=): dùng phép gán (=) để thay đổi 1 hoặc 1 đoạn phần tử tại chỉ số nào đó của list

v_list = [1, 4, 3, 7]
v_list[3] = 999
print(v_list)

# Thêm một phần tử vào list bằng phương thức append() hoặc thêm một list vào 1 list bằng phương thức extend().
# => Luôn luôn là thêm vào cuối list gốc trở đi

m_list = [0, 1, 2]
m_list.append(2000)
print(m_list)

m_list.extend([-3, -2, -1])
print(m_list)

m_list.append([0, 9, 2])
print(m_list)

# Chèn thêm 1 phần tử mưới vào list bằng phương thức insert(index, value)

h_list = [0, 2, 6, 7]
h_list.insert(2, 4)
print(h_list)

# Xóa một hoặc nhiều phần tử trong list sử dụng toán tử del

n_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# del n_list[3]
# del n_list[-6]
del n_list[-3:]
print(n_list)

# Ngoài ra còn có thể dùng remove(Phần_tử_muốn_xóa) hoặc pop(vị_trí_phần_tử_muốn_xóa)

j_list = [0, -1, -2, 8, 4, -5, 6, 7, 8, 9]
# j_list.remove(8) # Xóa đi phần tử đầu tiên từ trái sang phải
# print(j_list)
#
# j_list.remove(1999) # ValueError: list.remove(x): x not in list
# print(j_list)

x = j_list.pop(5) # <=> del j_list[5]
print(x)
print(j_list)


y = j_list.pop() # Xóa thằng cuối cùng
print(y)
print(j_list)

j_list.clear()
print(j_list)


'Phép toán cộng (+) 2 list để ra được list mới - chính là nối 2 list'
'Phép toán nhân list với số nguyên dương n, để ra được list mới lặp n lần'

print(h_list + [3, 2])
print(h_list * 3)

""" Danh sách các method của kiểu dữ liệu list
    - list.append(element): Thêm một phần tử element vào cuối list
    - list.extend(list2): Thêm nhiều phần tử trong list2 vào cuối của list
    - list.insert(index, element): Thêm phần tử element vào chỉ số index trong list
    - list.remove(element): Xóa phần tử element đầu tiên từ trái sang phải trong list nếu có, ko có sẽ lỗi
    - list.pop(index=-1): Xóa và trả lại giá trị phần tử tại chỉ số index
    - list.clear(): Xóa bỏ toàn bộ các phần tử => mảng rỗng
    - list.count(element): Đếm số lượng element trong list
    - list.reverse(): Đảo ngược list
    - list.sort(key=..., reverse=...): Sắp xếp list theo key nào đó, theo chiều tăng/giảm (reverse=True => giảm)
    <=> sorted(list, key=..., reverse=...)
    - list.copy(): Trả lại bản sao của list
"""

'Kiểm tra tồn tại'
''' 
    - in: Kiểm tra xem có trong list không
    - not in: Kiểm tra xem có trong list không
'''

'Duyệt list'
''' 
    Qua chỉ số của list
    Qua phép toán in (Trực tiếp)
'''


# List comprehension: Tạo ra list 1 cách tổng quát

'Ví dụ:Sinh ra list, chứa bình phương của các số từ 0 đến 9'
# Cách 1
result_list = []
for i in range(0, 10):
    result_list.append(i**2)
print(result_list)

# Cách 2
result_list1 = []
result_list1 = [i**2 for i in range(0, 10)]
print(result_list1)

'Ví dụ: Sinh ra list chứa các số chia hết cho 2 từ list cho trước'

random = [8, 1, 2, 5, 6, 0, 7, 9]
#Cách1 dùng append
#Cách 2: list comprehension
result = [x for x in random if x % 2 == 0]
print(result)


"""Quay lại chút với lambda function và sort, sorted, filter, map"""

your_list = ["abc", "1234", []]
your_list.sort(key=len)
print(your_list)

ran_list = ["abc", "1234", []]
ran_list.sort(key=len, reverse=True)
print(ran_list)

"""Với filter()
    - Nhận tham số là một function và 1 list
    - Tham số function sẽ được gọi với tất cả các phần tử của list và một list mới được trả ra chứa các phần tử
    mà tham số function xác định là True
"""
my_list = [1, 2, 5, 8, 9, 6, 7, 0]
# Lấy các phần tử là số chẵn trong list trên
so_chan_list = list(filter(lambda x: x % 2 == 0, my_list))
print(so_chan_list)

""" Với map()
    - Nhận tham số là một function và 1 list
    - Tham số function sẽ được gọi với tất cả các phần tử trong list và một list mới được trả ra chứa các phần tử
    mà được trả lại từ tham số function
"""
my_list = [1, 2, 5, 8, 9, 6, 7, 0]
# Tính bình phương các giá trị trong list
square_list = list(map(lambda x: x * x, my_list))
print(square_list)