#@author: leo jaimesson

import turtle

def wheat(size,pen):

    if(size < 1):
        return
    if(size == 50):
        pen.right(90)

    pen.backward(size)
    pen.backward(size)
    pen.backward(size)
    pen.backward(size)
    for x in xrange(0,4):
        x = pen.xcor()
        y = pen.ycor()
        angulo = pen.heading()
        pen.left(30)
        pen.backward(size * 0.2)
        wheat(size * 0.32, pen)
        pen.setpos(x, y)
        pen.setheading(angulo)
        pen.right(30)
        pen.backward(size * 0.2)
        wheat(size * 0.32, pen)
        pen.setpos(x, y)
        pen.setheading(angulo)
        pen.backward(-(size))


pen = turtle.Pen()
pen.color("white")
pen.screen.bgcolor("black")
pen.speed(30)

wheat(50, pen)


turtle.mainloop()