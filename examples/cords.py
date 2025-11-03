class Coords:
    def __init__(self, right=0, left=180, up=90):
        self.right = right
        self.left = left
        self.up = up

import turtle
t = turtle.Turtle()
t.reset
for x in range(1,2):
    position = Coords()
    t.left(position.right)
    t.forward(100)
turtle.done()
