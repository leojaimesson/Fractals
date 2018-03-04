#@author: leo jaimesson

import turtle

def ice(size,pen):
    if(size == 100):
        pen.left(90)
    if(size < 2):
        return
    for i in range(0,5):
        x = pen.xcor()
        y = pen.ycor()
        angulo = pen.heading()
        pen.backward(size)
        ice(size * 0.4, pen)
        pen.setpos(x,y)
        pen.setheading(angulo)
        pen.left(72)

pen = turtle.Pen()
pen.color("white")
pen.screen.bgcolor("black")
pen.speed(30)

ice(100, pen)


turtle.mainloop()