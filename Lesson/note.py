class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


a = Dog('Cookie', 3)
b = Dog('Brown', 2)

print(a.name)
print(a.speak('woof'))
print(a)


class Car:

    def __init__(self, color, mileage):
        self.color = color
        self.mileage = int(mileage)

    def __str__(self):
        return f"The {self.color} car has {self.mileage} miles."


blue_car = Car('Blue', 20000)
red_car = Car('Red', 30000)
print(blue_car)
print(red_car)


# Inherit From Other Classes in Python
class Bulldog(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)


class Dachshund(Dog):
    pass


class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)


# miles = Bulldog('Miles', 3)
# buddy = Dachshund('Buddy', 2)
# print(miles.species)
# print(buddy)
# print(miles.speak('Woof'))
# print(miles.speak('Grr'))
# print(isinstance(miles, Dog))
# print(isinstance(miles, Dachshund))

millie = GoldenRetriever('Millie', 5)
print(millie.speak())
