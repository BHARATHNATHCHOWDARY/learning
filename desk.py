from turtle import Turtle,Screen
import time

turtle=Turtle()
turtle.shape("square")
turtle.color("white")
turtle.penup()


screen=Screen()
screen.tracer(0)
screen.bgcolor("black")



def Up():
    turtle.setheading(90)
    turtle.forward(20)
def Down():
    turtle.setheading(270)
    turtle.forward(20)
def Left():
    turtle.setheading(180)
    turtle.forward(20)
def Right():
    turtle.setheading(0)
    turtle.forward(20)



screen.listen()
screen.onkey(Up,"Up")
screen.onkey(Down,"Down")
screen.onkey(Left,"Left")
screen.onkey(Right,"Right")


a=10
while a==10:
    screen.update()
    time.sleep(0.1)
    turtle.forward(20)

screen.exitonclick()


