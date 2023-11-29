import turtle

#Screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Bouncing Square")

#Border
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-300, -300)
mypen.pendown()
mypen.pensize(3)
mypen.color("white")
for side in range(4):
    mypen.forward(600)
    mypen.left(90)

mypen.hideturtle()

#square
square = turtle.Turtle()
square.shape("square")
square.color("white")
square.pencolor("green")
square.shapesize(stretch_wid=1, stretch_len=1, outline=1)
square.dy = 0
square.dx = 2
gravity = 0.26

#square activities
while True:
    square.dy -= gravity
    square.sety(square.ycor() + square.dy)
    square.setx(square.xcor() + square.dx)


    if square.ycor() < -290:
        square.sety(-290)
        square.dy *= -1
        square.shapesize(stretch_wid=square.shapesize()[0] + 1, stretch_len=square.shapesize()[1] + 1, outline=1)

    if square.ycor() > 290:
        square.sety(290)
        square.dy *= -1
        square.shapesize(stretch_wid=square.shapesize()[0] + 1, stretch_len=square.shapesize()[1] + 1, outline=1)

    if square.xcor() < -290:
        square.setx(-290)
        square.dx *= -1
        square.shapesize(stretch_wid=square.shapesize()[0] + 1, stretch_len=square.shapesize()[1] + 1, outline=1)

    if square.xcor() > 290:
        square.setx(290)
        square.dx *= -1
        square.shapesize(stretch_wid=square.shapesize()[0] + 1, stretch_len=square.shapesize()[1] + 1, outline=1)


    

    if not (-300 < square.xcor() < 300 and -300 < square.ycor() < 300):
        break
    






wn.mainloop()