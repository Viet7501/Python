"""
Xem code đã có trong file btvn_01_dog.py (link file đính kèm).
    Viết đoạn chương trình vào tiếp trong file đó để giải quyết yêu cầu sau:
        - Tạo ra 3 đối tượng Dog với các thuộc tính về age khác nhau:
            name        age
            Fake         2
            Mickey       7
            Fuk          5
        - Sau đó, viết một hàm get_biggest_number(*args) nhận vào nhiều tham số, sau đó trả về số lớn nhất.
        - Và dựa trên hàm này, hay tìm và in ra có dạng như sau:
            The oldest dog is 7 years old.
"""


def get_biggest_number(*age):
    oldest = max(age)
    print(f'The oldest dog is {oldest} years old')


class Dog:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def age(self):
        return self.age


first_dog = Dog('Fake', 2)
second_dog = Dog('Mickey', 7)
third_dog = Dog('Fuk', 5)
get_biggest_number(first_dog.age, second_dog.age, third_dog.age)


