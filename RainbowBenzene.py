#python module for using graphics
#create shapes or ddraw pictures
import turtle
turtle.bgcolor("black")
colors = ["red", "purple", "blue", "green", "orange", "yellow"]
turtle.speed(10)
for i in range(280):
    turtle.pencolor(colors[i%6])
    turtle.pensize(i/80 + 1)
    turtle.forward(i)
    turtle.left(59)
turtle.done()
