from turtle import Turtle, colormode, done

leo: Turtle = Turtle()

side_length: float = 300

colormode(255)
leo.color(99, 204, 250)

leo.penup()
leo.goto(45, 60)
leo.pendown()

leo.speed(50)
leo.hideturtle()

leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(side_length)
    leo.left(120)
    i = i + 1
leo.end_fill()

bob: Turtle = Turtle()
bob.color(0, 0, 0)
bob.speed(100)
bob.penup()
bob.goto(45, 60)
bob.pendown()
i: int = 0
while (i < 150):
    bob.forward(side_length)
    bob.left(121)
    side_length = side_length * 0.97
    i = i + 1
    

done()