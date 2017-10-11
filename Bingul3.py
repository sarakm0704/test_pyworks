import turtle

loadWindow = turtle.Screen()
turtle.colormode(255)

turtle.speed(0)

sides = 6

def shape(size, sides):
	for i in range(sides):
		turtle.forward(size)
		turtle.left(360/sides)
	
for i in range(50):
	shape(5*i,sides)
	turtle.left(i)


turtle.exitonclick()
