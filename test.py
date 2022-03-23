from turtle import *

speed(5)
bgcolor("indigo")

penup()
goto(-100, 0)
pendown()

# Squares
color("black", "white") # (outline, fill)
begin_fill()
for i in range(4):
    forward(200)
    right(90)
left(90)
for i in range(3):
    forward(200)
    right(90)
end_fill()

# Top Circle
penup()
goto(0, 130)
pendown()
color("black")
begin_fill()
circle(30)
end_fill()

# Bottom Circles
penup()
goto(-50, -20)
pendown()
begin_fill()
circle(30)
end_fill()

penup()
goto(50, -120)
pendown()
begin_fill()
circle(30)
end_fill()

hideturtle()