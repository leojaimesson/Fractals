#@author: leo jaimesson

import turtle

def tree(size, pen):
    if (size == 90):
        pen.left(90)
        pen.forward(size)

    if(size > 2):
        x = pen.xcor()
        y = pen.ycor()
        ang = pen.heading()
        pen.left(45)
        pen.forward(size * 0.7)
        tree(size * 0.7, pen)
        pen.up()
        pen.setx(x)
        pen.sety(y)
        pen.setheading(ang)
        pen.down()
        pen.right(45)
        pen.forward(size * 0.7)
        tree(size * 0.7, pen)



pen = turtle.Pen()
pen.color("white")
pen.screen.bgcolor("black")
pen.speed(30)

tree(90, pen)

turtle.mainloop()