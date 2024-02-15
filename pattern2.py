from turtle import *
speed(0)

def polygon(side, size):
    for i in range(side):
        fd(size)
        lt(360/side)

# calling
 for i in range(6):
    polygon(6,50)
    lt(60)
mainloop()