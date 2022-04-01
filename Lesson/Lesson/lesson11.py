"""
Một đối tượng có hai đặc trưng:
- Thuộc tính (attributes)
- Hành vi (behavior)

"""

""" 
    xét ví dụ sau: Cat là một đối tượng có:
    - tên, tuổi, màu lông ==> Thuộc tính
    - kêu, chạy, nhảy, ăn, uống ==> Hành vi
"""
#
#
# class Cat:
#
#     def __init__(self, ten, tuoi, mau_long):
#         self.ten = ten
#         self.tuoi = tuoi
#         self.mau_long = mau_long
#
#     def my_cat(self):
#         print(f'Con mèo màu {self.mau_long} này tên {self.ten}, {self.tuoi} tuổi')
#
#     def keu(self):
#         print(f"{self.ten} kêu meow meow")
#
#     def chay(self):
#         print(f'{self.ten} đang chạy ')
#
#
# cat1 = Cat('Bin', 2, 'đen')
# cat1.my_cat()
# cat1.keu()

""" 
    - OOP tập trung vào việc viết code có thể tái sử dụng - DRY - Dont Repeat Yourself
    - Trong Python, OOP theo một số nguyên tắc cơ bản như sau:
        . Inheritance - Kế thừa: Sử dụng các chi tiết từ một class mới mà không làm thay đổi gì class đã có
        . Encapsulation - Đóng gói: Ẩn các chi tiết riêng tư của một class đối với các object khác
        . Polymorphism - Đa hình: Sử dụng các thao tác chung theo nhiều cách khác nhau tương ứng với các đầu vào
         khác nhau.
"""

"""         Inheritance - Kế thừa 
        - Là cách tạo ra class mới có sử dụng chi tiết từ class đã có mà không thay đổi nó
        - Lớp mới được gọi là lớp dẫn xuất (hoặc lớp con), lớp đã có là lớp cơ sở (hoặc lớp cha)

            class (the most) base là object
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def who_am_i(self):
        print('Person')

    def speak(self, lang='Tiếng Việt'):
        print(f'{self.name} nói {lang}')


person_1 = Person('Duy', 20)
person_1.speak()


class StudentIT(Person):
    def __init__(self, name, age, school):
        # self.name = name
        # self.age = age
        super().__init__(name, age)
        self.school = school

    # def speak(self, lang='Tiếng Việt'):
    #     print(f'{self.name} nói {lang}')
    def who_am_i(self):
        print('StudentIT')

    def code(self, pro_lang):
        print(f'{self.name} lập trình {pro_lang}')


sv = StudentIT('Việt LQ', 18, 'HUST')
sv.speak()
sv.code('Python')
sv.who_am_i()
sv.age = 40

"""         Encapsulation - Đóng gói 
    - Trong Python, có thể hạn chế quyền truy cập vào các phương thức và biến
      ==> ngăn dữ liệu không bị sửa đổi trực tiếp ==> được gọi là Đóng gói - Encapsulation
    - Dùng ký hiệu cho thuộc tính private là 2 gạch dưới __
"""


class Laptop:

    def __init__(self):
        self.__price = 500  # Thuộc tính private

    def sell(self):
        print(f'Giá bán là {self.__price}')

    def set_price(self, new_price):  # Hàm setter
        if new_price >= 0.7 * self.__price:
            self.__price = new_price
        else:
            print(f'{new_price} is wrong')


mb_pro = Laptop()
mb_pro.sell()

mb_pro.__price = 1000  # Không thể thay đổi __price của mb_pro
mb_pro.sell()

mb_pro.set_price(1000)
mb_pro.sell()

mb_pro.set_price(100)
mb_pro.sell()

"""         Polymorphism - Đa hình
    - Là khả năng (trong OOP) cho phép dùng chung interface cho nhiều hình thái (kiểu dữ liệu)
    - Ví dụ cho dễ hiểu: Cần tô màu cho một hình, có nhiều hình: vuông, tròn, chữ nhật,...; nhưng
    có thể dùng cùng một phương thức để tô màu cho hình ==> Đây chính là đa hình 
"""


def connect_wifi(computer):
    computer.wifi()


class PC:
    def wifi(self):
        print('Không kết nối được!')


class Laptop:
    def wifi(self):
        print('Kết nối thành công!')


pc = PC()
lap = Laptop()

connect_wifi(pc)
connect_wifi(lap)

""" Method Overriding - Ghi đè phương thức
    - Trong chương trình trên thấy, __init__() được định nghĩa trong cả 2 class.
    - Điều gì xảy ra, khi method trong class dẫn xuất ghi đề lên class cơ sở
    => __init__() trong lớp dẫn xuất được ưu tiên hơn trong class cơ sở
    - Khi ghi đè, thường chúng ta mong muốn mở rộng nó chứ không đơn thuần là thay thế nó.
    Điều tương tự cũng được thực hiện khi gọi phương thức class cơ sở từ trong class dẫn xuất DaGiac.__init__(self, 3) từ __init__() của TamGiac
    Một cách tốt hơn làm việc này là dùng super()
            DaGiac.__init__(self, 3)  <=>  super().__init__(3)
"""
""" Python cung cấp isinstance() và issubclass() để kiểm tra tính kế thừa
    isinstance() - trả lại True nếu object là thể hiện của class hoặc của class dẫn xuất từ nó.
                   Tất cả các class trong Python đều được kế thừa từ class có tên là object
    issubclass() - kiểm tra kế thừa của 2 class
"""


""" Kế thừa đa cấp - Multilevel Inheritance
    - Có thể dùng kế thừa từ một lớp dẫn xuất => kế thừa đa cấp. Trong Python, độ sâu bao nhiêu cũng được
    - Trong kế thừa đa cấp, toàn bộ trong class cơ sở và class dẫn xuất được kế thừa lại cho class dẫn xuất mới
    - Cú pháp:
        class Base:
            thân_của_Base
        class Derived1(Base):
            thân_của_Derived1
        class Derived2(Derived1):
            thân_của_Derived2
"""

# derived 2 cấp thứ 4, class Base là con của object


"""     Đa kế thừa - Multiple Inheritance
    - Giống như một số ngôn ngữ lập trình khác (như C++...), Python cung cấp đa kế thừa
    - Một class có thể được kế thừa từ nhiều class cơ sở
    - Tất cả các thứ của các lớp cơ sở đều kế thừa lại cho class dẫn xuất
    - Cú pháp
    
    class Base1:
        thân_của_Base1
    
    class Base2:
        thân_của_Base2
        
    class MultiDerived(Base1, Base2):
        thân_của_MultiDerived
"""

""" Thứ tự các Resolution
    - Mọi class trong Python đều kế thừa từ class object - đây là class cơ sở nhất
    - Về mặt kỹ thuật, tất cả các class (kể cả dựng sẵn hay do người dùng định nghĩa) đều là class dẫn xuất của class object,
    và tất cả các đối tượng đều là thể hiện của class object => Ví dụ dưới
    - Trong kích bản đa kế thừa, bất kì thuộc tính nào đầu tiên cũng được tìm kiếm tại class hiện tại, nếu không thấy,
    sẽ tìm kiếm lên các lớp cha theo độ ưu tiên: chiều sâu - trước rồi từ trái qua phải, đảm bảo ko tìm kiếm cùng 1 class 2 lần
    Ví dụ: MultiDerived được tìm kiếm theo thứ tự [Base1, Base2, object] - tuyến tính hóa của class MultiDerived,
    quy tắc ngày được gọi là Method Resolution Order (MRO) - Thứ tự phân giải phương thức
    - MRO đảm bảo 1 class luôn xuất hiện trước cha của nó. Được hiển thị bằng thuộc tính __mro__ hoặc phương thức mro() => Ví dụ dưới
"""


"""     Class or Static Variable: 
    - Được khai báo trong class nhưng bên ngoài các method
    - Được truy cập thông qua class chứ không cần object
    - Biến class/static là khác biệt và không conflict với các thuộc tính khác cùng tên
"""


class Pet:
    total = 0   # class/static variable

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
        Pet.total += quantity


dog = Pet('Dog', 5)
print(dog.total)
cat = Pet('Cat', 4)
print(cat.total)
python = Pet('Python', 2)
print(python.total)
# print(f'Total : {dog.quantity + cat.quantity + python.quantity}')
print(f'Total PET : {Pet.total}')


"""     @staticmethod:
    - Với việc dùng decorated trên thì tạo ra static method, và chia sẻ namespace với class
    - Method này không yêu cầu tham số bắt buộc nào, còn đối với object method thì có self là bắt buộc
    - Truy cập được vào các biến tĩnh của lớp 
"""


class ExampleStatic:
    name = 'ExampleStatic'  #static variable

    @staticmethod
    def static_method():
        print(f'>>> {ExampleStatic.name} static_method() called')


ExampleStatic.static_method()


"""     Tổng kết buổi hôm nay
 3 nguyên tắc cơ bản lập trình hướng đối tượng
 method overriding
 kế thừa đa cấp và đa kế thừa - Method Resolution Order
 class/static variable và static method

"""