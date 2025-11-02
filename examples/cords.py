#first try didn't work


# import turtle
# t = turtle.Turtle()
# t.reset
# for x in range(1,2):
	# self = t.forward(100)
	# self
# turtle.done()
	
# class Coords:
	# def _int_(self, x1=20, y1=67, x2=0, y2=0):
	    # self.x1 = x1
	    # self.y1 = y1
	    # self.x2 = x2
	    # self.y2 = y2


#second try worked I think on the first try I kindof was thinking about it wrong.
# import numpy
import numpy as np
a = np.array([1, 2, 3])
# using np.coords() method
gfg = a.flat
next(gfg)
print(gfg.coords)
