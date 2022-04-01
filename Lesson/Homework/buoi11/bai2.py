"""
Xem code đã có trong file btvn_02_pet.py (file trong link đính kèm).
    Viết đoạn chương trình vào tiếp trong file đó để giải quyết yêu cầu sau:
        - Hãy tạo ra class Pet để chứa các đối tượng của class Dog, class Pet này độc lập với
        class Dog (hay Pet ko kế thừa từ Dog)
        - Sau đó, tạo 4 đối tượng kiểu Dog và gán thành thuộc tính của 1 đối tượng kiểu Pet
            name        age
            Tom          6
            Jerry        9
            Butt         3
            Wine         1
        - Code đoạn chương trình để in ra được như sau:
            I have 4 dogs.
            Tom is 6. Jerry is 9. Butt is 3. Wine is 1.
            And they're all mammals, of course.
"""


# class Pet:
#     def __init__(self):
#         self.dog1 = self.Dog('Tom',6)
#         self.dog2 = self.Dog('Jerry',9)
#         self.dog3 = self.Dog('Butt',3)
#         self.dog4 = self.Dog('Wine',1)
#
#     def print_me(self):
#         print('I have 4 dogs')
#         print(self.dog1.description(), self.dog2.description(), self.dog3.description(), self.dog4.description(), sep='. ')
#         print(f"And they're all {self.dog1.species} of course")
#
#     class Dog:
#         species = 'mammal'
#
#         def __init__(self, name, age):
#             self.name = name
#             self.age = age
#
#         def description(self):
#             return f'{self.name} is {self.age} years old'
#
#         def speak(self, sound):
#             return f'{self.name} says {sound}'
#
#     class RussellTerrier(Dog):
#         def run(self, speed):
#             return f'{self.name} runs {speed}'
#
#     class Bulldog(Dog):
#         def run(self, speed):
#             return f'{self.name} runs {speed}'
#
#
# pet = Pet()
# pet.print_me()


class Dog:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f'{self.name} is {self.age} years old'

    def speak(self, sound):
        return f'{self.name} says {sound}'


class RussellTerrier(Dog):
    def run(self, speed):
        return f'{self.name} runs {speed}'


class Bulldog(Dog):
    def run(self, speed):
        return f'{self.name} runs {speed}'


class Pet:

    def __init__(self):
        self.dogs = []  #List các object của Dog


dog1 = Dog('Tom', 6)
dog2 = Dog('Jerry', 9)
dog3 = Dog('Butt', 3)
dog4 = Dog('Wine', 1)

pet = Pet()
pet.dogs = [dog1, dog2, dog3, dog4]

print(f'I have {len(pet.dogs)} dogs')
for dog in pet.dogs:
    print(dog.description(), end='. ')
print()
print(f"And they're all {Dog.species}, of course ")