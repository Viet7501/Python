"""
    Để mô phỏng được yếu tố may rùi (ngẫu nhiên) thì chúng ta có thể dùng đến module random
"""

# import random
#
# # for roll in range(10):  # lặp 10 lần
# #     print(random.randrange(1, 7), end=' ')
#
# # Ví dụ: kiểm tra xem khả năng (xác suất) xảy ra của các mặt có phải thực sự ngẫu nhiên hay không
# list1 = []
# n = int(input())
# for roll in range(n):
#     list1.append(random.randrange(1, 7))
#
# dem = {}
#
# for i in list1:
#     if i in dem:
#         dem[i] += 1
#     else:
#         dem[i] = 1
# print(dem)

""" OOPs trong Python
    - Python là một trong những ngôn ngữ lập trình đa mô hình => Python sẽ hỗ trợ nhiều phương pháp lập trình khác nhau
    - Một trong những phương pháp tiếp cận phổ biến hiện nay là Hướng đối tượng - Object-Oriented Programming (OOP)
    - Một đối tượng có hai đặc trưng:
        - Thuộc tính (attributes)
        - Hành vi (behavior)
    - Xét ví dụ sau:
        Cat là một đối tượng có:
        - tên, tuổi, màu lông => Thuộc tính
        - kêu, chạy, nhảy, ăn, uống => Hành vi
    - Khái niệm OOP trong Python còn tập trung vào việc viết code có thể tái sử dụng, được biết đến như là DRY - Dont Repeat Yourself
    - Trong Python, OOP theo một số nguyên tắc cơ bản như sau:
        - Inheritance - Kế thừa: Sử dụng các chi tiết từ một class mới mà ko làm thay đổi gì class đã có
        - Encapsulation - Đóng gói: Ẩn các chi tiết riêng tư của một class đối với các object khác
        - Polymorphism - Đa hình: Sử dụng các thao tác chung theo nhiều cách khác nhau tương ứng với các đầu vào khác nhau
"""

""" Class - Là bản thiết kế cho object
    - Có thể hình dùng class như một bản phác thảo của một cat với các nhãn. Nó chứa tất cả chi tiết về name, age, ...
    - Dựa trên các mô tả đó, chúng ta sẽ đi tìm hiểu về cat, ở đây, cat là một object
"""

""" Object
    - Một object (instance) là một khởi tạo của một lớp
    - Khi class được định nghĩa, thì chỉ có các mô tả của object được xác định
    => không có bộ nhớ hoặc lưu trữ nào được phân bổ
"""

''' 
        **class, object là gì?**
    - Python là ngôn ngữ lập trình trình hướng đối tượng 'thuần'. Là ngôn ngữ lập trình hướng đối tượng
nên trọng tâm của nó là đối tượng - object    
    
        **object**: là tập các dữ liệu (biến) và các phương thức để hoạt động trên các dữ liệu đó
        **class**: là bản thiết kế cho objeobject
    - Mỗi *object* được gọi là *íntance (thể hiện)* cho class, việc tạo ra object được gọi là
*instantiation - khởi tạo*     
'''

# Khai báo class
""" 
 - Bắt đầu bằng từ khóa 'class', sau đó là 'tên của class'
 - Đoạn string đầu tiên được gọi là docstring - mô tả cho class (không bắt buộc)
 - Mỗi class sẽ tạo ra một không gian cục bộ mới, nơi mà thuộc tính của nó được định nghĩa. Thuộc tính gồm: data
hoặc function
- Ngoài ra, còn có các thuộc tính đặc biệt được định nghĩa bắt đầu bằng 2 gạch dưới __, ví dụ: __doc__ trả lại docstring của class đó
- Ngay khi định nghĩa class, thì một class object mới được tạo ra với cùng tên.
    Cái này giúp cho phép truy cập các thuộc tính và khởi tạo đối tượng mới cho class đó => Xem ví dụ 2
"""


class MyClass:
    """
    Đây là docstring của class
    """
    attribute = 0

    def func(self, name):
        print(f'Hello {name} ')


print(MyClass.attribute)  # Truy cập vào data
print(MyClass.func)  # Truy cập vào function
print(MyClass.__doc__)
# Tạo ra object
""" 
    - Mỗi class object dùng để truy cập vào thuộc tính khác nhau
    - Nó cũng có thể dùng để tạo ra các object mới (thể hiện của class). Cách dùng như một lời gọi hàm => Ví dụ 3: Tạo ra
    một object có tên là obj. Có thể truy cập đến các thuộc tính của object bằng cách dùng tên của object đó.
    - Thuộc tính có thể là data hoặc method. Method của một object là các hàm tương ứng của class. Bất kì function object
    nào là thuộc tính của class đều được xác định là một method cho object của class đó.
    Điều này có nghĩa là MyClass.func là một function object (attribute của class), obj.func là method object
"""
""" Method - Là các định nghĩa hàm bên trong thân class, dùng để định nghĩa hành vi của object """


""" 
    - Dùng tên của class như 1 lời gọi hàm (ví dụ dưới)
"""

obj = MyClass()  # Khởi tạo obj từ MyClass

print(MyClass.func)
print(obj.func)  # Truy cập vào method của object
print(obj.attribute)

obj.func('Python')  # obj là self trong khi call func() => func(obj)
# MyClass.func(obj, 'Python') # tương đương câu lệnh trên

"""Để ý, trong class, có tham số self trong định nghĩa function, nhưng khi gọi obj.func() lại ko cần tham số => nó vẫn chạy
Điều này là do, bất cứ khi nào một đối tượng gọi method của nó, chính là sẽ được truyền làm tham số đầu tiên
Vì vậy, obj.func() được dịch thành MyClass.func(obj)
=> Túm lại thì, việc gọi phương thức với 1 list n tham số là việc gọi hàm tương ứng với list tham số được tạo ra bằng cách
thêm object trước tham số đầu tiên. Vì vậy, đối số đầu tiên của hàm trong class phải là chính đối tượng đó,
điều này được gọi là self, có thể dùng từ khác nhưng khuyên chân thành là nên tuân theo quy ước dùng self.
Giờ thì đã biết đến: class object, instance object, function object, method object (và sự khác nhau giữa chúng)"""




"""     *Hàm khởi tạo - Constructor*
    - Hàm khởi tạo trong tất cả các class đều là __init()__
    - Được gọi mỗi khi một object được tạo ra class
    - Nếu không khai báo cụ thể thì sẽ có "hàm mặc định" được gọi
"""

# Khai báo class mô tả về phân số trong toán: tử số và mẫu số
import math


class Fraction():

    def __init__(self, tu, mau):
        self.tu_so = tu
        self.mau_so = mau

    def show(self):
        print(f'Phân số: {self.tu_so}/{self.mau_so}')

    def cong(self, ps):
        _tu = self.tu_so * ps.mau_so + ps.tu_so * self.mau_so
        _mau = self.mau_so * ps.mau_so
        return Fraction(_tu, _mau)

    def simply(self):
        _gcd = math.gcd(self.tu_so, self.mau_so)
        self.tu_so = self.tu_so / _gcd
        self.mau_so = self.mau_so / _gcd


ps1 = Fraction(2, 3)  # Khai báo object ps1 với thuộc tính: tu_so=2, mau_so=3
ps1.show()

ps1.mau_so += 4
ps1.tu_so -= 10
ps1.show()


ps2 = Fraction(1, 2)
ps3 = Fraction(1, 3)
ps4 = ps2.cong(ps3)
ps4.show()

ps5 = Fraction(6, 9)
ps5.simply()
ps5.show()

ps6 = Fraction(1, 3)
ps7 = Fraction(1, 6)
ps8 = ps6.cong(ps7)
ps8.simply()
ps8.show()

# Trong đoạn code trên, định nghĩa một class mới Fraction biểu diễn cho phân số, có hai hàm
# __init__() để khởi tạo các biến tử số và mẫu số, mặc định là 0 và 1
# và show() để hiển thị phân số đúng cách
# Một thứ rất thú vị, thuộc tính của một đối tượng có thể được tạo ra khi đang chạy chương trình.
# Thấy thuộc tính attr của ps2 được tạo ra và được đọc bình thường, còn ps1 thì ko có, cố tính truy cập sẽ báo lỗi


""" Xóa bỏ thuộc tính và đối tượng
    - Bất kì thuộc tính nào của đối tượng cũng có thể bị xóa bỏ đi bất cứ lúc nào bằng cách dùng câu lệnh del => Ví dụ 5
"""

# Ví dụ 5:
ps3 = Fraction(2, 5)
del ps3.mau_so
ps3.show()  # AttributeError: 'Fraction' object has no attribute 'mau_so'

del Fraction.show
ps3.show()  # AttributeError: 'Fraction' object has no attribute 'show'

ps4 = Fraction(5, 9)
del ps4
ps4  # NameError: name 'ps4' is not defined

# Giải thích: xóa bỏ đối tượng, trong thực tế cũng khá phức tạp
# Khi tạo ra ps4 = Fraction(5, 9) một đối tượng của Fraction được tạo ra trong memory và ps4 được gắn với nó
# Trong lệnh, del ps4 cái liên kết gắn đó bị xóa và tên ps4 được xóa bỏ khỏi không gian các tên biến.
# Và đối tượng thì vẫn tồn tại trong memory, khi ko còn tên nào được gắn với nó thì nó sẽ bị hủy tự động
# Việc hủy tự động các đối tượng không có tham chiếu này trong Python được gọi là bộ sưu tập rác - garbage collection