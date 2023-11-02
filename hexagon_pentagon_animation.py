import turtle
import math 

def draw_hexagon(size):
    """Draw a hexagon with given size."""
    turtle.left(30)
    for _ in range(6):
        turtle.forward(size)
        turtle.left(60)
    turtle.right(30)  # Return to the original orientation


def move(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def draw_triangle(size, direction="right"):
    """Draws a triangle inside the hexagon."""
    turtle.color("red")

    if direction == "right":
        turtle.forward(size)
        turtle.right(120)
        turtle.forward(size)
        turtle.right(120)
        turtle.forward(size)
        turtle.right(120)
    elif direction == "left":
        turtle.forward(size)
        turtle.left(120)
        turtle.forward(size)
        turtle.left(120)
        turtle.forward(size)
        turtle.left(120)


def draw_square(size, direction):
    """Draw a square of given size and direction."""
    # Determine the rotation angle based on the hexagon's side
    if direction == "clockwise":
        angle = -90
    else:  # anticlockwise
        angle = 90
    for _ in range(4):
        turtle.forward(size)
        turtle.left(angle)

def move_to_edge(size, edge_count, direction):
    """Moves the turtle to a specified edge of the hexagon."""
    turn_angle = 60 if direction == "clockwise" else -60
    for _ in range(edge_count):
        turtle.forward(size)
        turtle.left(turn_angle)

def draw_pattern():
    turtle.speed(5)
    turtle.width(3)
    size = 200

    # Draw the central hexagon
    # draw_hexagon(size)
    
    # Draw squares around the hexagon
    for _ in range(6):
        move_to_edge(size, 1, "clockwise")
        draw_square(size, "anticlockwise")

    # Draw the first triangle
    turtle.right(270)
    draw_triangle(math.sqrt(3) * size, "right")

    turtle.penup()
    turtle.right(90)
    turtle.forward(size)
    turtle.pendown()
    turtle.right(270)
    draw_triangle(math.sqrt(3) * size, "left")


    turtle.penup()
    turtle.left(90)
    turtle.forward(size/2)
    x, y = turtle.pos()
    turtle.right(90)
    turtle.forward((math.sqrt(3) * size)/3)
    turtle.right(30)
    turtle.pendown()
    draw_triangle((math.sqrt(3) * size)/3.58, "left")
    
    turtle.penup()
    turtle.left(-150)
    turtle.forward((math.sqrt(3) * size)/3)
    turtle.right(90)
    turtle.forward(size/2)
    turtle.right(60)
    turtle.forward(size/2)
    turtle.right(90)
    turtle.forward((math.sqrt(3) * size)/3)
    turtle.right(30)
    turtle.pendown()
    draw_triangle((math.sqrt(3) * size)/3.58, "left")

    move(x, y)
    turtle.penup()
    turtle.left(90)
    turtle.forward((math.sqrt(3) * size)/5.8)
    turtle.pendown()

    turtle.color("cyan")

    turtle.left(-90)
    draw_hexagon((math.sqrt(3) * size)/3)

    move(x, y)
    turtle.right(0)
    turtle.penup()
    turtle.forward(size/2)
    turtle.left(-330)
    turtle.pendown()
    draw_hexagon(size)

    turtle.done()

screen = turtle.Screen()
screen.bgcolor("black")
turtle.color("white")
draw_pattern()
 
