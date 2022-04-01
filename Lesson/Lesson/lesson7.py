# coding=utf-8
__author__ = "hoanbk02@gmail.com"
__copyright__ = "Copyright 2020, Phạm Phú Hoàn"

""" Tuple:
    - Introduction
    - Accessing Tuple
    - Operations
    - Working with Tuple
    - Functions and Methods
"""
""" ==>> Tuple cũng khá giống với List.
    Điều khác duy nhất là: Tuple ko thể thay đổi các phần tử trong nó còn List thì ngược lại.
"""

""" Cách tạo Tuple: Đặt các phần tử trong cặp ngoặc tròn () và cách nhau bởi dấu phẩy
    => Ngoặc tròn có thể được bỏ qua, nhưng mới bắt đầu thì nên tuân thủ đúng điều trên
"""
empty_tuple = ()  # Tuple rỗng
print(empty_tuple)
my_tuple = (-1, 2, 0, 3)  # Tuple chứa các số nguyên
print(my_tuple)
your_tuple = (1, 'Hi', 'Night!', 2.718, 1+3j)  # Tuple chứa phần tử mang nhiều kiểu dữ liệu
print(your_tuple)
our_tuple = (1992, [1, 0, 3, -5], (), ('Py', 'js', 0, 3.14))  # Tuple dạng lồng nhau
print(our_tuple)

# Tạo Tuple không cần dùng cặp ngoặc tròn  => Kỹ thuật Tuple packing
mine_tuple = 'cat', 1999, 'pig', 1996
print(mine_tuple)

# => unpacking
a, b, c, d = mine_tuple
print(f"a = {a}, b = {b}, c = {c}, d = {d}")

# Việc tạo một Tuple có 1 phần tử hơi khó khăn chút và dễ bị nhầm lẫn
one_tuple = ('one element')  # có gợi ý từ IDE, và đang hiểu đây là String ko phải Tuple
print(one_tuple)
a_tuple = ('one element', )  # như này mới hiểu là Tuple 1 phần tử, chú ý dấu phẩy
print(a_tuple)
tuple_01 = 'one element',   # đây cũng được hiểu là Tuple 1 phần tử với việc không dùng ngoặc tròn
print(tuple_01)


""" Truy cập vào trong Tuple
    - Bằng chỉ số dương: Dùng toán tử [] và đưa chỉ số phần tử muốn truy cập. Chỉ số bắt đầu từ 0 đến (số phần tử - 1).
    Với Tuple lồng nhau thì dùng chỉ số lồng nhau.
    - Bằng chỉ số âm: Dùng toán tử [] và đưa chỉ số dạng âm của phần tử muốn truy cập.
    Chỉ số âm đánh từ phải sang trái, bắt đầu là -1 cho phần tử cuối cùng, và ngược đến -(số phần tử) cho phần tử đầu tiên
    - Đoạn cắt: Dùng toán tử [] kết hợp với toán tử : để có thể lấy ra 1 đoạn các phần tử của tuple
"""
your_tuple = (1, 'Hi', 'Night!', 2.718, 1+3j)
print(len(your_tuple))  # Số lượng phần tử của your_tuple
print(your_tuple[4])
print(your_tuple[0])

our_tuple = (1992, [1, 0, 3, -5], (), ('Py', 'js', 0, 3.14))
print(our_tuple[1])
print(our_tuple[1][2])
print(our_tuple[3][1])

my_tuple = ('py', 'thon', 'java', 'script', 'Ox', 'Oy')
print(my_tuple[-2])
print(my_tuple[-6])

my_tuple = ('py', 'thon', 'java', 'script', 'Ox', 'Oy')
print(my_tuple[:4])
print(my_tuple[2:])
print(my_tuple[1:4])
print(my_tuple[:-5])


""" Thay đổi, cập nhật Tuple. Không giống như List, Tuple là kiểu dữ liệu không cho phép thay đổi (giống String).
    - Điều này có nghĩa là các phần tử không thể bị thay đổi.
    Nhưng nếu phần tử trong một Tuple lồng mà là dạng dữ liệu có thể thay đổi thì ta có thể thực hiện thay đổi được (<= Khá dị)
    - Có thể thực hiện gán giá trị mới cho biến Tuple cũ (reassignment)
    - Ghép 2 Tuple bằng cách dùng dấu +
    - Nhân 1 Tuple với 1 số nguyên dương n => lặp lại Tuple đó lên n lần
"""

my_tuple = (1992, [1, 0, 3, -5], (26, 10, 1999))
# my_tuple[2] = 2000  # Lỗi: TypeError: 'tuple' object does not support item assignment
my_tuple[1][3] = 5
print(my_tuple)

my_tuple = ('re', 'assignment', 'reassignment')
print(my_tuple)

tuple_01 = (1, 2, 3)
tuple_02 = (4, 5, 6)
tuple_03 = (7, 8, 9)
print(tuple_01 + tuple_02 + tuple_03)
print(tuple_01 * 2)
print(tuple_01)
print(tuple_02)
print(tuple_03)


""" Xóa phần tử Tuple
    - Như trên đã nói, chúng ta ko thể thay đổi các phần tử trong Tuple => không thể xóa phần tử trong Tuple
    - Tuy nhiên, có thể xóa hoàn toàn 1 tuple bằng từ khóa del
"""
my_tuple = (0, 1, 2, 3, 4, 5)
# del my_tuple[3]  # Lỗi: TypeError: 'tuple' object doesn't support item deletion

del my_tuple  # Xóa hoàn toàn tuple đi
# print(my_tuple)  # Lỗi: NameError: name 'my_tuple' is not defined


""" Các phương thức của Tuple
    - Do không phải kiểu dữ liệu có thể thay đổi => add và remove không thể tồn tại trong kiểu dữ liệu Tuple
    - Chỉ còn 1 phương thức
        - tuple.count(element): Đếm số lượng phần tử element trong tuple
        - tuple.index(element): Trả lại chỉ số của phần tử element đầu tiên từ trái sang phải
"""
my_tuple = ('d', 'o', 'g', 'p', 'i', 'g', 'd', 'u', 'c', 'k')
print(my_tuple.count('g'))
print(my_tuple.index('d'))

""" Các toán tử khác của Tuple
    - Kiểm tra có thuộc Tuple hay không: in hoặc not in
    - Duyệt một Tuple với for và in
"""
my_tuple = ('d', 'o', 'g', 'p', 'i', 'g')
print('a' in my_tuple)
print('i' in my_tuple)
print('h' not in my_tuple)

love_tuple = ("HAT", 'MT', 'HNH', 'TH')
for singer in love_tuple:
    print(f"I like {singer}")

for i in range(len(love_tuple)):
    print(f"I like", love_tuple[i])

""" Một số ƯU ĐIỂM của Tuple so với List.
Theo các thứ đã trao đổi, Tuple khá giống với List và chúng thường được sử dụng trong các tình huống tương tự nhau.
Tuy nhiên, vẫn có một số ưu điểm khi sử dụng Tuple so với List như sau:
    - Thường dùng Tuple chứa các phần tử với các kiểu dữ liệu không đồng nhất (khác nhau)
    Còn List chứa các phần tử với kiểu dữ liệu đồng nhất (giống nhau)
    - Tuple là kiểu dữ liệu immutable (bất biến/ko thay đổi được), thì duyệt nó sẽ nhanh hơn List => Tăng cường hiệu năng
    - Tuple có chứa các phần tử immutable, có thể dùng làm key cho dictionary, với List thì không thể
    - Nếu có dữ liệu không được thay đổi, dùng Tuple sẽ đảm bảo được tính chất đó, nó sẽ chống ghi đè
"""

# coding=utf-8
__author__ = "hoanbk02@gmail.com"
__copyright__ = "Copyright 2020, Phạm Phú Hoàn"

""" Set:
    - Introduction
    - Accessing Set
    - Operations
    - Working with Set
    - Functions and Methods
"""
""" Set là gì?
    - Là tập hợp các phần tử không có thứ tự. Mỗi phần tử là duy nhất (ko trùng lặp) và phải bất biến (ko thay đổi được)
    - Nhưng, bản thân Set thì lại không bất biến, có nghĩa là có thể thêm, sửa, xóa phần tử của chính nó
    - Được sử dụng như tập hợp trong Toán học, với các phép toán: Hợp, Giao, Phần bù, ... 
"""

""" Cách tạo ra Set:
    - Được tạo ra bằng cách để các phần tử trong cặp ngoặc {} và cách nhau bởi dấu phẩy hoặc sử dụng hàm gốc set()
    - Có thể chứa nhiều phần tử với các kiểu dữ liệu khác nhau: integer, float, tuple, string, ....
    Nhưng không chứa phần tử không bất biến kiểu như list, set, dictionary.
"""
my_set = {1, 2, 3, 5, 9}  # Set chứa số nguyên
print(my_set)

your_set = {'Morning', 0, 3.14, (1, 2, 0, 'Py')}  # Set chưa hỗn hợp các kiểu
print(your_set)

# Cố tính tạo Set chứa phần tử lặp vào trong Set
our_set = {1, 0, 0, 1, 2}
print(our_set)

# Cố tính tạo ra Set chứa phần tử không bất biến
fuk_set = {[1, 0, 3], 9}  # Lỗi: TypeError: unhashable type: 'list'
print(fuk_set)

fake_set = {}  # Đây không phải set rỗng, mà là dictionary rỗng
print(type(fake_set))  # Not empty set, is dictionary
empty_set = set()  # Khai báo Set rỗng
print(type(empty_set))


""" Thêm phần tử vào Set như nào?
    - Set là không bất biến - có thể thay đổi được. Nhưng nó ở dạng không có thứ tự, nên không dùng chỉ số được.
    => Ko truy cập bằng chỉ số hoặc đoạn cắt được.
    - Có thể dùng add() để thêm 1 phần tử mới hoặc dùng update() để thêm nhiều phần tử.
    update() thì có thể truyền vào tuple, list, string hoặc một set khác. Mặc định thì sẽ loại bỏ được trùng lặp
"""
my_set = {0, 1, 3, 4}
print(my_set)

# Cố tình dùng chỉ số
print(my_set[0])  # Lỗi: TypeError: 'set' object does not support indexing

my_set.add(2)
print(my_set)

my_set.update([2, 3, 4])
print(my_set)

my_set.update([0, 1], [9, 8, 3])
print(my_set)


""" Xóa phần tử trong Set như nào?
    - Một phần tử cụ thể có thể được xóa khỏi Set bằng hàm discard() hoặc remove()
    Hai hàm này khác nhau ở chỗ: nếu phần tử muốn xóa không tồn tại trong Set thì remove() sẽ báo lỗi,
     discard() thì không
    - Xóa đi và trả lại phần tử bất kì nào đó trong Set dùng pop()
    - Xóa đi toàn bộ Set dùng clear() trả lại set rỗng
"""
my_set = {1, 4, 5, 6, 2, 0, 3}
print(my_set)
my_set.discard(5)
print(my_set)
my_set.remove(4)
print(my_set)

# Cố tính xóa đi phần tử không tồn tại trong Set
my_set.discard(9)
my_set.remove(8)

your_set = {'python', 1, 0, 'lập trình'}
print(your_set.pop())
print(your_set)

your_set.clear()
print(your_set)


""" Các toán tử dùng với Set. Set có thể được dùng như Tập hợp trong toán học
    - union - hợp: Hợp của 2 Set là một Set chứa tất cả các phần tử của 2 Set. Tính chất: A hợp B = B hợp A
    - intersection - giao: Giao của 2 Set là một Set chứa tất cả các phần tử chung của 2 Set. Tính chất A giao B = B giao A
    - difference - phần bù: Phần bù của Set A so với Set B là một Set chứa các phần tử trong A nhưng không có trong B
    - symmetric difference - phần bù đối xứng: Phần bù đối xứng của 2 Set là một Set chứa toàn bộ những phần tử có trong cả 2 set,
    bỏ đi các phần tử chung của 2 Set. Tính chất: A bù đối xứng B = B bù đối xứng A
"""
set_01 = {0, 1, 2, 3, 4, 5, 6}
set_02 = {5, 6, 7, 8, 9, 0, 1}

print(set_01 | set_02)
print(set_01.union(set_02))
print(set_02.union(set_01))

print(set_01 & set_02)
print(set_01.intersection(set_02))
print(set_02.intersection(set_01))

print(set_01 - set_02)
print(set_01.difference(set_02))
print(set_02 - set_01)

print(set_01 ^ set_02)
print(set_02.symmetric_difference(set_01))


""" Các phương thức của Set
    - set.add(element): Thêm một phần tử element vào set
    - set.clear(): Xóa toàn bộ các phần tử của set thành set rỗng
    - set.copy(): Trả lại một bản sao của set
    - set.difference(*other_set): Trả lại một set là phần bù của 2 hoặc nhiều set
    - set.difference_update(other_set): Cập nhật lại set bằng các giá trị phần bù của set với other_set (nếu có)
    - set.discard(element): Xóa một phần tử element trong set (ko làm gì nếu như element ko tồn tại trong set)
    - set.intersection(*other_set): Trả lại giao của 2 hoặc nhiều set
    - set.intersection_update(other_set): Cập nhật lại set bằng các giá trị giao giữa nó và other_set
    - set.isdisjoint(other_set): Trả lại True nếu set và other_set không giao nhau
    - set.issubset(other_set): Trả lại True nếu set là con của other_set
    - set.issuperset(other_set): Trả lại True nếu set có chứa other_set
    - set.pop(): Xóa và trả lại một phần tử ngẫu nhiên trong set. Trả lại KeyError nếu như set rỗng
    - set.remove(element): Xóa element khỏi set, nếu element không tồn tại sẽ báo lỗi KeyError
    - set.symmetric_difference(*other_set): Trả lại phần bù đối xứng của 2 hoặc nhiều set
    - set.symmetric_difference_update(other_set): Cập nhật lại set bằng các giá trị phần bù đối xứng giữa nó và other_set
    - set.union(*other_set): Trả lại hợp giữa 2 hoặc nhiều set
    - set.update(other_set): Cập nhật set bằng hợp giữa nó và other_set
"""

# Bài tập: Viết chương trình để thử lại các phương thức của Set vừa nói trên


""" Các toán tử khác trong Set
    - Kiểm tra tồn tại trong Set: in
    - Kiểm tra không tồn tại trong Set: not in
    - Dùng for và in để duyệt toàn bộ Set
"""
my_set = {1, 0, 3, 2, 4}
print(2 in my_set)
print('x' not in my_set)

apple_set = set('apple')  # chuyển đổi các ký tự trong String thành phần tử của Set
for char in apple_set:
    print(char)


""" Các hàm dựng sẵn với Set (List và cả các kiểu dữ liệu có thể iterable)
    - all(): Trả lại True nếu như tất cả các phần tử là True hoặc nó rỗng
    - any(): Trả lại True nếu như bất kì phần tử nào đó là True, trong trường hợp rỗng thì return False
    - enumerate(): Trả lại một đối tượng kiểu enumerate (liệt kê). Nó chứa các cặp gồm chỉ số và giá trị tương ứng
    - len(): Trả lại số lượng phần tử
    - max(): Trả lại giá trị lớn nhất
    - min(): Trả lại giá trị nhỏ nhất
    - sorted(): Sắp xếp các phần tử trả lại giá trị ra, ko tác động lên biến gốc
    - sum(): Trả lại tổng các phần tử
"""
# Bài tập: Viết chương trình để thử lại các phương thức vừa nói trên với cả kiểu dữ liệu Set và List

""" Python Frozenset
    - Là một class mới có đặc tính như một Set, nhưng các phần tử của nó thì không thể thay đổi nếu như đã được gán.
    Tuple là kiểu chứa List bất biến, còn frozensets là kiểu chứa Set bất biến.
    - Set không bất biến ko được hash nên không thể dùng để làm key trong dictionary,
     còn frozensets thì có được hash nên hoàn toàn dùng được.
    - frozensets được tạo ra bằng hàm frozenset()
    - Có phương thức: copy(), difference(), intersection(), isdisjoint(), issubset(), 
                      issuperset(), symmetric_difference(), union()
    Vì là bất biến nên không cung cấp hàm add() và remove()
"""

my_frozenset = frozenset([0, 1, 2, 3, 5, 6, 3])
your_frozenset = frozenset([2, 3, 4, 7, 4, 1])
print(my_frozenset)
my_frozenset.isdisjoint(your_frozenset)
your_frozenset.difference(my_frozenset)
print(my_frozenset | your_frozenset)

# my_frozenset.add(1992)  # Lỗi: AttributeError: 'frozenset' object has no attribute 'add'