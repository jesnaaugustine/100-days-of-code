from turtle import Turtle,Screen
import turtle
import random
tim = Turtle()
turtle.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

def draw_circle(tilt):
    for i in range(int(360/tilt)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() +tilt)

if __name__ =='__main__':
    tim.speed("fastest")
    draw_circle(5)
    

    screen = Screen()
    screen.exitonclick()

