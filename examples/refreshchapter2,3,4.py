import random
import turtle
t = turtle.Turtle()

def drawshapes():
    n = input('say how many shapes you want:')
    m = input('what percent are circles:')
    count = 0
    for x in range(0,int(n)):
            
        if random.random() < int(m)/100:
            t.forward(10)
            t.circle(10)
            t.forward(20)
            count=count+1
        else:
            for x in range(0,5):
                t.forward(10)
                t.right(90)
            t.forward(20)  
    print('"turtle\'s shapes include',count,'circles"')
    turtle.done()
drawshapes()
