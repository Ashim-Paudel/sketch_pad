import turtle as t
import random

t.colormode(255)

tut = t.Turtle()    # created a turtle object
screen = t.Screen()   # created a screen object


def clockwise_circle():
    tut.speed('fastest')
    tut.right(10)
    tut.forward(10)


def anticlock_circle():
    tut.speed('fastest')
    tut.left(10)
    tut.forward(10)


def random_color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    tut.color(r, g, b)


def clear_screen():
    tut.clear()


screen.onkeypress(lambda: tut.forward(10), key="Up")     # move forward by 10 paces
screen.onkeypress(lambda: tut.bk(10), key="Down")   # move back by 10 paces
screen.onkey(lambda: tut.right(90), "Right")   # turns right by 90 degree
screen.onkey(lambda: tut.left(90), "Left")       # turns left by 90 degree
screen.onkeypress(lambda: tut.penup(), key="space")   # not-write mode by pressing space
screen.onkeyrelease(lambda: tut.pendown(),  key='space')  # write mode when not pressed space
screen.onkeypress(lambda: tut.right(10), key='r')    # turn right by 10 paces on clicking 'r' key
screen.onkeypress(lambda: tut.left(10), key='l')   # turn left by 10 paces on clicking 'l' key
screen.onkeypress(fun=clockwise_circle, key="R")    # draws a circle in clockwise direction on "R" key
screen.onkeypress(fun=anticlock_circle, key='L')   # draws a circle in anticlockwise direction  "L" key
screen.onkeypress(lambda: tut.pensize(1), key='t')   # increase the pensize of turtle
screen.onkeypress(lambda: tut.pensize(10), key='T')  # decrease the pensize
screen.onkey(fun=random_color, key="c")      # change colors randomly on pressing c
screen.onkey(lambda: tut.color('black'), key='b')  # set back the black color on pressing b
screen.onkey(fun = clear_screen, key="C")  # clear whole screen


screen.listen()
screen.exitonclick()
