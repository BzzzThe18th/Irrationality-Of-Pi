import turtle 
import math
import numpy as np

pen = turtle.Turtle() 
pen.hideturtle()
pen.penup()

outerPen = turtle.Turtle()
outerPen.hideturtle()
outerPen.penup()

radius1 = input("Radius of inner circle: ")
if radius1 == '': radius1 = 150
else: radius1 = float(radius1)
radius2 = input("Radius of outer circle: ")
if radius2 == '': radius2 = 150
else: radius2 = float(radius2)
speed = input("Speed of rotation (choppier with speed): ")
if speed == '': speed = 1
else: speed = float(speed)
bgColor = input("Background color in hex: ")
if bgColor == '': bgColor = '#1c1c1c'
color = input("Line color in hex: ")
if color == '': color = '#ffffff'
input("Press ENTER to begin the visualization")

turtle.bgcolor(bgColor)
outerPen.color(color)

i = 0
while True:
    pen.goto(radius1 * math.cos(i / 30 * speed), radius1 * math.sin(i / 30 * speed))
    outerPen.goto(turtle.Vec2D(pen.pos()[0] + radius2 * math.cos(i / 30 * speed * np.pi), pen.pos()[1] + radius2 * math.sin(i / 30 * speed * np.pi)))
    outerPen.pendown()
    i += 1