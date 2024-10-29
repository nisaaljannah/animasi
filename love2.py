import turtle
import time

# Set up the screen
wn = turtle.Screen()
wn.title("Love Animation")
wn.bgcolor("white")

# Create turtle for drawing heart
heart = turtle.Turtle()
heart.shape("turtle")
heart.color("red")
heart.speed(2)

# Function to draw a heart shape
def draw_heart():
    heart.begin_fill()
    heart.left(50)
    heart.forward(133)
    heart.circle(50, 200)
    heart.right(140)
    heart.circle(50, 200)
    heart.forward(133)
    heart.end_fill()

# Function to create heart animation effect
def heart_animation():
    for _ in range(10):
        heart.penup()
        heart.goto(0, -50)
        heart.pendown()
        draw_heart()
        heart.clear()  # Clear the screen for the next heart
        time.sleep(0.5)  # Pause before drawing the next heart

# Run the heart animation
heart_animation()

# Finish
heart.hideturtle()
turtle.done()
