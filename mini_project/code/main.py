from helper import *


background("G:/Python/mini_project/hello.png")
character("G:/Python/mini_project/anh.png")

print('Welcome! What would you like for me to do?')
user_choice = input()


color("blue")
pensize(5)
pendown()
circle(100)
penup()
backward(30)
left(90)
forward(130)
dot(30)
right(90)
penup()
forward(60)
dot(30)
left(90)
backward(60)
right(90)
backward(60)
right(90)
pendown()
circle(30,180)
penup()
backward(110)
right(90)
backward(170)


color("red")
write(user_choice, font=('arial', 15))
left(90)
penup()
forward(60)
