import turtle

tt = turtle.Turtle()
tt.shape('turtle')
tt.shapesize(1,1,1)

for i in range(40):
	tt.circle(5*i)
	tt.circle(-3*i)
	tt.left(i)

