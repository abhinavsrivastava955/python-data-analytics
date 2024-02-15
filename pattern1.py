from  turtle import *
speed(0)
def square():
    for i in range (4):
        forward(100)
        right(90)

def hexagon():
    for i in range(6):
        forward(100)
        right(60)

for i in range(6):
    fd(100)
    hexagon()
    rt(60)
hideturtle()
mainloop()