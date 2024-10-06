import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.title("Line and Curve")
screen.bgcolor("white")

# Create a turtle object
pen = turtle.Turtle()
pen.speed(2)

# Function to draw a line
def draw_line(length):
    pen.forward(length)

# Function to draw a curve (semi-circle)
def draw_curve(radius):
    pen.circle(radius, 180)

# Draw a line
pen.color("blue")
draw_line(150)

pen.penup()
pen.goto(-50, -50)
pen.pendown()
pen.color("red")
draw_curve(100)

# Close the window when clicked
turtle.done()
