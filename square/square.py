#@author: leo jaimesson

import turtle

def square(size , pen):
    if (size > 200):
        return
    pen.forward(size)
    pen.right(90)
    square(size + 2, pen)

pen = turtle.Pen()
pen.color("white")
pen.screen.bgcolor("black")
pen.speed(30)

square(1, pen)


turtle.mainloop()