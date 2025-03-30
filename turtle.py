import turtle
import time

win = turtle.Screen()
win.title("Tiny's Adventure")

tiny = turtle.Turtle()  # Define tiny as a Turtle object

def print_text(text):
    global tiny
    tiny.clear()
    tiny.penup()
    tiny.goto(-200, 200)
    tiny.pendown()
    tiny.write(text, font=("Arial", 16, "normal"))

tiny.shape("turtle")  # Set the shape of the turtle
tiny.speed(1)  # Set the speed of the turtle

print_text("Once upon a time in a faraway place...")
time.sleep(3)
tiny.forward(100)

print_text("Lived a little turtle named Tiny.")
time.sleep(2)
tiny.left(90)
tiny.forward(100)

print_text("Tiny loved to explore and go on adventures.")
time.sleep(2)
tiny.right(90)
tiny.forward(100)

print_text("One day, Tiny decided to explore the forest.")
time.sleep(2)
tiny.left(90)
tiny.forward(100)

print_text("She met a friendly rabbit who offered her some carrots.")
time.sleep(2)
tiny.right(90)
tiny.forward(100)

print_text("Tiny was so happy and full that she fell asleep.")
time.sleep(2)
tiny.penup()
tiny.goto(-200, -200)
tiny.pendown()
print_text("The end.")

turtle.done()

