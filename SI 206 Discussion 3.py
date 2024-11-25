from turtle import *

# Drawing a filled circle
def draw_filled_circle(turtle, x, y, radius, color):
    turtle.penup()
    turtle.goto(x, y - radius)  # Adjust for the center of the circle
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

# Drawing a rectangle
def draw_rectangle(turtle, x, y, width, height, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

# Draw smiley face
def draw_emoji(turtle):
    # Face
    draw_filled_circle(turtle, 0, 0, 100, 'yellow')

    # Sunglasses
    draw_rectangle(turtle, -70, 50, 50, 30, 'black')
    draw_rectangle(turtle, 20, 50, 50, 30, 'black')
    draw_rectangle(turtle, -20, 60, 60, 10, 'black')

    # Mouth
    turtle.penup()
    turtle.goto(-45, -20)
    turtle.setheading(-60)
    turtle.pendown()
    turtle.pencolor('black')
    turtle.pensize(5)
    turtle.circle(50, 120)  # Arc for smile

def main():
    # Setup screen
    screen = Screen()
    screen.bgcolor("orange")  # Set background color to orange
    screen.title("Turtle Emoji")

    # Create turtle
    t = Turtle()
    t.speed("fastest")

    # Draw emoji
    draw_emoji(t)

    # Wait for user to close the window
    screen.exitonclick()

if __name__ == '__main__':
    main()
