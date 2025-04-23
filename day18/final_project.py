from turtle import Turtle,Screen
import turtle
import random
tim = Turtle()
tim.penup()
tim.hideturtle()

tim.setheading(225)
tim.forward(500)
tim.setheading(0)

turtle.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

if __name__=='__main__':
    for i in range(20):
        for j in range(20):
            tim.dot(10,random_color())
            tim.forward(50)
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(1000)
        tim.setheading(0)

    screen = Screen()
    screen.exitonclick()
    

