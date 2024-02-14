from turtle import *

speed('fastest')
pencolor('blue')
pensize(4)
for i in range(6):
    fd(120)
    lt(360/6)
    write(f'n={i}')

hideturtle()
mainloop()