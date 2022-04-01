from turtle import *
screen = Screen()

screen.setup(400, 400)

shape("turtle")
penup()

def background(image):
    screen.bgpic(image)

def character(image):
    screen.addshape(image)
    shape(image)