from turtle import Turtle,Screen
import turtle as t
import random
turtle =Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g= random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color
def draw(side):
    turtle.color(random_color())
    for _ in range(side):
        turtle.right(360/side)
        turtle.forward(100)
if __name__=='__main__':
    for i in range(3,10):
        draw(i)


    screen = Screen()
    screen.exitonclick()