from turtle import *
speed(0)

def sierpinski (l, n) :
    if n==0 :
        begin_fill() #fill space with color
        forward (l)
        left (120)
        forward (l)
        left (120)
        forward (l)
        left (120)
        end_fill ()
    else :
        sierpinski (l/2, n-1)
        forward (l/2)
        sierpinski (l/2, n-1)
        left (120)
        forward (l/2)
        right (120)
        sierpinski (l/2, n-1)
        right (120)
        forward (l/2)
        left (120)

setworldcoordinates(-50, -50, 700, 700)
rang=0
rang = numinput("Sierpinski Triangle", "What stage ?", rang, minval=0, maxval=100)
sierpinski(500, rang)
exitonclick()

