"""
Giải quyết yêu cầu sau:
        - Thêm thuộc tính is_hungry = True cho class Dog
        - Thêm một method eat() để thay đổi giá trị cho is_hungry thành False khi nó được gọi đến
        - Kiểm tra và in ra
            My dogs are not hungry.
        nếu như tất cả các Dog trong Pet đều có is_hungry = False, ngược lại thì in ra
            My dogs are hungry.
        - Cuối cùng có thể in ra được kiểu như sau:
            I have 4 dogs.
            Tom is 6. Jerry is 9. Butt is 3. Wine is 1.
            And they're all mammals, of course.
            My dogs are not hungry.
"""


class Pet:
    def __init__(self):
        self.dog1 = self.Dog('Tom', 6, False)
        self.dog2 = self.Dog('Jerry', 9, True)
        self.dog3 = self.Dog('Butt', 3, False)
        self.dog4 = self.Dog('Wine', 1, False)

    def print(self):
        print('I have 4 dogs')
        print(self.dog1.description(), self.dog2.description(), self.dog3.description(), self.dog4.description(),
              sep='. ')
        print(f"And they're all {self.dog1.species} of course")

    def hungry(self):
        if self.dog1.is_hungry is False & self.dog2.is_hungry is False & self.dog3.is_hungry is False & self.dog4.is_hungry is False:
            print('My dogs are not hungry')
        else:
            print('My dogs are hungry')

    class Dog:
        species = 'mammal'

        def __init__(self, name, age, is_hungry):
            self.name = name
            self.age = age
            self.is_hungry = True

        def description(self):
            return f'{self.name} is {self.age} years old'

        def speak(self, sound):
            return f'{self.name} says {sound}'

        def eat(self):
            if self.is_hungry is True:
                self.is_hungry = False

    class RussellTerrier(Dog):
        def run(self, speed):
            return f'{self.name} runs {speed}'

    class Bulldog(Dog):
        def run(self, speed):
            return f'{self.name} runs {speed}'


pet = Pet()
pet.print()

pet.hungry()
pet.dog1.eat()
pet.dog2.eat()
pet.dog3.eat()
pet.dog4.eat()
pet.hungry()
