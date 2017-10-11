import turtle
g = turtle.Turtle()
g.shape('turtle')
g.shapesize(2,2,3)

g.home()
g.clear()
g.penup()
g.forward(200)
g.left(90)
g.pendown()
g.circle(200)
g.penup()
g.home()
g.pendown()

import random
while True:
	g.left(random.randint(1,360))
	g.forward(15)
	if g.distance(0,0) > 200:
		g.undo()

