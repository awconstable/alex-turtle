from turtle import *

turtle = Turtle()
screen = Screen()
turtle.speed(100)

color = input('What color do you want?')
turtle.pencolor(color)

loops = input('How many loops do you want?')
i = 0

while i in range(int(loops)):
    turtle.circle(50)
    turtle.right(30)
    turtle.forward(100)
    i += 1

screen.exitonclick()
screen.listen()
