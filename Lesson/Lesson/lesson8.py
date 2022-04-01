'''
    Dictionary
        Introdiction
        Accessing dict
        Working with dict
        Properties
        Functions and Methods
'''

'Làm thế nào để tạo ra một dict ?'
''' 
    Đặt các phần tử trong cặp ngoặc nhọn {}, cách nhau bởi dấu phẩy
    Mỗi phần tử key và value được biểu thị dưới dạng key: value
    value có thể mang bất kì kiểu dữ liệu nào và có thể trùng lặp;còn key thì
    chỉ được dùng kiểu dữ liệu bất biến(string, number hoặc tuple với các phần tử bất biến) và không lặp
'''

my_dict = {
    1: 'Một',
    2: 'Hai',
    3: 'Ba'
}
print(my_dict)
print(type(my_dict))

your_dict = {
    'name' : 'Python',
    1: [9, 8, 3, 0]
}
print(your_dict)

# our_dict = {
#     [1, 2, 3]: 'List'   # TypeError: unhashable type: 'list'
# }

''' 
    Truy cập vào dict
        Các kiểu dữ liệu trước đây, nếu có thể thì dùng chỉ số để truy cập
        Còn dict thì dùng key để truy cập
        Có thể dùng toán tử [] hoặc hàm get()
        get() sẽ trả lại None nếu như key ko tồn tại, còn [] sẽ trả lại lỗi: KeyError
'''

her_dict = {
    'name' : 'Python',
    'level' : 'high',
    'age' : 30
}

print(her_dict['name'])
print(her_dict.get('age'))

print(her_dict.get('phone'))
# print(her_dict['phone'])    #KeyError: 'phone'

''' 
    Thay đổi hoặc thêm mới phần tử:
        dict là kiểu không bất biến
        Có thể thêm mới hoặc thay đổi giá trị của phần tử đã tồn tại bằng toán tử gán (=)
        Nếu key đã tồn tại thì value được cập nhật, ngược lại thì thêm cặp key: value mới
'''

his_dict = {
    'name' : 'Duck',
    'age' : 2
}

his_dict['age'] = 10  # thay đổi value của key = age
print(his_dict)

his_dict['age'] += 2 # Câp nhật value của age lên 2 đơn vị
print(his_dict)

his_dict['phone'] = '0912345678' # thêm mới phần tử phone : 0912345678 vào dict
print(his_dict)

his_dict['phone'] = '0987654321'
print(his_dict)

''' 
    Xóa phần tử
        - Có thể xóa một phần tử cụ thể bằng cách dùng pop(key), xóa khỏi dict
    phần tử có key và trả lại value của phần tử đó
        - popitem() dùng để xóa và trả về cặp (key, value) ở vị trí cuối cùng của dict
        - clear() dùng để xóa toàn bộ các phần tử
        - Toán tử del để xóa phần tử cụ thể nào đó
'''

m_dict = {
    1: -1,
    2: -2,
    3: -3,
    4: -4,
    5: -5
}

v = m_dict.pop(3)
print(v)

item = m_dict.popitem()
print(item)

m_dict.clear()
print(m_dict)


''' 
        Các phương thức của dict
   - clear(): Xóa toàn bộ phần tử, thành dict rỗng
    - copy(): Tạo bản sao cho dict
    - fromkeys(seq[, v]): Trả lại dict mới với các key từ seq và giá trị từ v, nếu không có thì mặc định = None
    - get(key[,d]): Trả lại value của key, nếu key ko tồn tại thì trả lại d, nếu ko có d thì trả lại None
    - pop(key[,d]): Xóa và trả lại value của phần tử có key, nếu không tồn tại key thì trả lại d, nếu ko có d thì báo lỗi KeyError
    - popitem(): Trả lại phần tử bất kì dạng (key, value), nếu dict rỗng thì báo lỗi KeyError
    - items(): Trả lại thể hiện của dict dạng (key, value)
    - keys(): Trả lại List các key của dict
    - values(): Trả lại list các giá trị của các phần tử trong dict
    - setdefault(key[,d]): Nếu key tồn tại, trả lại value, nếu ko thêm key với value=d và trả lại d, nếu ko có d thì là None
    - update([other]): Cập nhật dict với các cặp key-value trong other, nếu key tồn tại thì sẽ ghi đè     
    
'''

l_dict = {
    1: -1, 2: -2, 3: -3, 4: -4, 5: -5
}

a = l_dict.get(10, -10)
print(a)

_items = l_dict.items()
_keys = l_dict.keys()
_values = l_dict.values()
print(_items)
print(_keys)
print(_values)

print(l_dict)
l_dict.update({
    10: -10,
    5: -50
})
print(l_dict)

l_dict = {}.fromkeys([1, 3, 5, 2])
print(l_dict)

m_dict = {}.fromkeys([1, 3, 5, 2], 'Value chung')
print(m_dict)

h_dict = {
    1: -1, 2: -2, 3: -3, 4: -4, 5: -5, 1: 0 # nếu key trùng nhau, lấy thằng cuối tương tự như update
}

print(h_dict)

x_dict = {
    1: -1, 2: -2, 3: -3, 4: -4, 5: -5
}

print("Test phương thức setdefault:", x_dict.setdefault(0, 100))
print(x_dict)


''' 
    Các  toán tử khác làm việc với dict
        in: Kiểm tra xem key có trong dict hay ko
        not in: Kiểm tra xem key đó có trong dict
        for và in để duyệt dict
'''

test_dict = {1: -1, 2: -2, 3: -3}

print('Cách 1, Duyệt trực tiếp')
for k in test_dict: # lấy lần lượt các key ra
    print(f'{k} : {test_dict[k]}')

print('Cách 2: Duyệt qua keys')
for k in test_dict.keys():
    print(f'{k} : {test_dict[k]}')

print('Cách 3: Duyệt qua ítems')
for k, v in test_dict.items():
    print(f'{k}: {v}')



test1_dict = {1: -1, 2: -2, 3: -3, 4: -5, 5: -100, 6: 'Python'}

print('Duyệt trực tiếp')
for k in test1_dict:
    print(f'{k} : {test1_dict[k]}')


'Dictionary Comprehension: Tạo dict một cách bao quát'
''' 
    Tạo dict mới từ việc duyệt lặp
    Dạng lệnh: cặp key:value theo sau là for, tất cả được đặt trong {}
    Trong for có thể chứa nhiều for khác hoặc chứa if
'''

ab_dict = {}
for i in range(10):
    ab_dict[i] = i**2

print(ab_dict)

ac_dict = {i: i**2 for i in range(10)}
print(ac_dict)

bc_dict = {i: i**2 for i in range(10) if i % 3 == 0}
print(bc_dict)


list_keys = [1, -2 , -4, -5, 3, 0, 2, 6]
list_values = [1, -2 , -4, -5, 3, 0, 2, 6]

o_dict = {list_keys[i]: list_values[-i - 1] for i in range(len(list_keys))}
# o_dict = {}
# for i in range(len(list_keys)):
#     o_dict[list_keys[i]] = list_values[-i-1]
#
print(o_dict)


""" Các phương thức dựng sẵn làm việc với dict
    - all(): Trả lại True nếu các key trong dict là true, hoặc là dict rỗng
    - any(): Trả lại True nếu có bất kì key nào đó true, nếu dict rỗng thì trả lại False
    - len(): Trả lại số lượng phần tử trong dict
    - sorted(): Trả lại một list đã sắp xếp của các key
"""
# Hãy viết chương trình để kiểm chứng lại hoạt động của các hàm trên

my_dict = {1: 2, 0: 3, 4: 5}
print(sorted(my_dict))

a_contact = {
    'first_name': 'Pham',
    'last_name': 'Hoan',
    'cell': '0912614123',
    'home': '0362286624',
    'address': 'Ha Noi',
    'company': 'Teko'
}

my_dict = {
    1: ['a', 'b'],
    2: [2, 4, 6, 5],
    3: {1: 1, 2: 2},
    (1, 2): 10
}
print(my_dict)