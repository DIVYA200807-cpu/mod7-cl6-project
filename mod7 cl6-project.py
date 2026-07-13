import turtle
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Colour Loop Artwork")


pen = turtle.Turtle()
pen.speed(0)
pen.pensize(3)
pen.hideturtle()


colours = [
    "red",
    "orange",
    "yellow",
    "green",
    "cyan",
    "blue",
    "purple",
    "pink"
]


def draw_petal(colour):
    pen.color(colour)
    pen.begin_fill()
    for i in range(2):
        pen.circle(100, 60)
        pen.left(120)
    pen.end_fill()


pen.penup()
pen.goto(0, 0)
pen.pendown()


for i in range(32):
    draw_petal(colours[i % len(colours)])
    pen.left(11.25)


pen.penup()
pen.goto(0, -20)
pen.pendown()
pen.color("gold")
pen.begin_fill()
pen.circle(20)
pen.end_fill()


turtle.done()