class Coords:
    def __init__(self, right=0, left=180, up=90 , down=270):
        self.right = right
        self.left = left
        self.up = up
        self.down = down

times = 2

import turtle
t = turtle.Turtle()
t.reset
while times < 10:
    position = Coords()
    direction = input('choose left up right or down say restet to restart or say any color of the rainbow:')
    if direction == 'left':
        t.left(position.left)
        t.forward(100)
        t.left(180)
    if direction == 'right':
        t.left(position.right)
        t.forward(100)
    if direction == 'up':
        t.left(position.up)
        t.forward(100)
        t.left(270)
    if direction == 'down':
        t.left(position.down)
        t.forward(100)
        t.left(90)
    if direction == "reset":
        t.reset()
        times = times
    if direction == 'red':
        t.pencolor("red")
    if direction == 'orange':
        t.pencolor("orange")
    if direction == 'yellow':
        t.pencolor("yellow")
    if direction == 'green':
        t.pencolor('green')
    if direction == 'blue':
        t.pencolor("blue")
    if direction == 'purple':
        t.pencolor("purple")


turtle.done()
