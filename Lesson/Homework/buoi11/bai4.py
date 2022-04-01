""" Xem code đã có trong file btvn_04_dog_walking.py.
Giải quyết yêu cầu sau:
        - Thêm method walk() vào class Pet và Dog. Khi gọi đến hàm walk() trong Pet thì vỡi mỗi đối tượng của Dog
        trong Pet sẽ gọi đến hàm walk() tương ứng.
        - Viết đoạn chương trình để in ra như sau:
            Tom is walking!
            Jerry is walking!
            Butt is walking!
"""


class Pets:

    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs

    def walk(self):
        print(f'{self.dogs} is walking!')


class Dog:
    species = 'mammal'
    is_hungry = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f'{self.name} is {self.age} years old'

    def speak(self, sound):
        return f'{self.name} says {sound}'

    def eat(self):
        self.is_hungry = False

    def walk(self):
        print(f'{self.name} is walking!')


class RussellTerrier(Dog):
    def run(self, speed):
        return f'{self.name} runs {speed}'


class Bulldog(Dog):
    def run(self, speed):
        return f'{self.name} runs {speed}'


dog1 = Dog('Tom', 6)
dog2 = Dog('Jerry', 9)
dog3 = Dog('Butt', 3)

Pets.dogs.append(dog1.name)
Pets.dogs.append(dog2.name)
Pets.dogs.append(dog3.name)

for i in Pets.dogs:
    pet = Pets(i)
    pet.walk()

    