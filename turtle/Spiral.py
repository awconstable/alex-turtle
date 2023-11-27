import turtle

t = turtle.Turtle()
screen = turtle.Screen()
turtle.speed("fastest")
r = 10
for i in range(100):
    t.circle(r + i, 45)

screen.exitonclick()
screen.listen()
