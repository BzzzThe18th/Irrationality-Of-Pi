import turtle 
import math
import numpy as np

outerAngle = 0
pen = turtle.Turtle() 
outerPen = turtle.Turtle()
pen.hideturtle()
pen.penup()
outerPen.hideturtle()
outerPen.penup()

radius1 = float(input("Radius of inner circle: "))
radius2 = float(input("Radius of outer circle: "))
speed = float(input("Speed of rotation: "))
input("Press ENTER to begin the visualization")

i = 0
while True:
    pen.goto(radius1 * math.cos(i / 30 * speed), radius1 * math.sin(i / 30 * speed))
    outerPen.goto(turtle.Vec2D(pen.pos()[0] + radius2 * math.cos(i / 30 * speed * np.pi), pen.pos()[1] + radius2 * math.sin(i / 30 * speed * np.pi)))
    outerPen.pendown()
    i += 1