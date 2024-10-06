import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.title("Basic Shapes")
screen.bgcolor("white")

# Create a turtle object
pen = turtle.Turtle()
pen.speed(2)  # Set the speed of the turtle

# Function to draw a square
def draw_square(side_length):
    for _ in range(4):
        pen.forward(side_length)
        pen.right(90)

# Function to draw a rectangle
def draw_rectangle(width, height):
    for _ in range(2):
        pen.forward(width)
        pen.right(90)
        pen.forward(height)
        pen.right(90)

# Function to draw a circle
def draw_circle(radius):
    pen.circle(radius)

# Function to draw a triangle
def draw_triangle(side_length):
    for _ in range(3):
        pen.forward(side_length)
        pen.left(120)

# Draw shapes
pen.color("blue")
draw_square(100)

pen.penup()
pen.goto(-150, 0)
pen.pendown()
pen.color("red")
draw_rectangle(150, 100)

pen.penup()
pen.goto(150, 150)
pen.pendown()
pen.color("green")
draw_circle(50)

pen.penup()
pen.goto(-150, -150)
pen.pendown()
pen.color("purple")
draw_triangle(100)

# Close the window when clicked
turtle.done()
