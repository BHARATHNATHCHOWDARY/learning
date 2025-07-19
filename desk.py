from turtle import Turtle,Screen

turtle=Turtle()
turtle.shape("square")

screen=Screen()
screen.listen()
screen.onkey()
screen.exitonclick()

def Up():
    turtle.setheading(90)
def Down():
    turtle.setheading(270)
def Left():
    turtle.setheading(180)
def Right():
    turtle.setheading(0)
