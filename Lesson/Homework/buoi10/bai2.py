"""
Viết một chương trình để lấy ra tên class của một object?
"""


class MyClass:
    """
    Đây là docstring của class
    """
    attribute = 0

    def func(self, name):
        return name


obj = MyClass()
print(type(obj).__name__)