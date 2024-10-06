# shapes-curves-and-line-in-python
How to draw shapes, lines and curves in python
Drawing a Line and a Curve
First, we set up the screen and turtle again:

screen = turtle.Screen()
screen.title("Line and Curve")
screen.bgcolor("white")

pen = turtle.Turtle()
pen.speed(2)
This part is exactly the same as before. We import the turtle tool, set up a blank screen with a white background, and create a turtle called pen.
Drawing a line:
def draw_line(length):
    pen.forward(length)
The draw_line(length) function tells the turtle to draw a straight line.
pen.forward(length) moves the turtle forward by the amount of "length" you give it, drawing a line as it goes.
________________________________________
Drawing a curve:
def draw_curve(radius):
    pen.circle(radius, 180)
The draw_curve(radius) function tells the turtle to draw a curve, like part of a circle.
pen.circle(radius, 180) draws part of a circle. The 180 means the turtle will only go halfway around the circle (making a semi-circle or curve).
Now Finally, the turtle starts drawing:
pen.color("blue")
draw_line(150)

pen.penup()
pen.goto(-50, -50)
pen.pendown()
pen.color("red")
draw_curve(100)
pen.color("blue") changes the pen color to blue before drawing the line.
draw_line(150) makes the turtle draw a straight line that's 150 units long.
After that, we move the turtle to a new position using pen.penup() and pen.goto(-50, -50) so it won’t draw while moving.
Then we put the pen back down with pen.pendown() and change the color to red using pen.color("red").
draw_curve(100) draws a curve (a half-circle) with a radius of 100.

And in the end
turtle.done()
This line keeps the window open so you can see the drawing. It won’t close until you close it yourself.

So essentially, Functions are reusable instructions that make our turtle draw specific shapes.
We move the turtle around with pen.forward() to draw lines, and we turn it with pen.right() or pen.left().
pen.circle() makes the turtle draw a full or partial circle.
By changing the turtle’s color, we can make our shapes more colorful.




