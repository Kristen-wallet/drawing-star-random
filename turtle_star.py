import turtle as t
from random import random,randint

def draw_star(size,points,color,x,y):
    angle = 180-(180/points)
    t.penup()
    t.goto(x,y)
    t.speed(5)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for i in range(points):
        t.forward(size)
        t.right(angle)
    t.end_fill()

#main code
count = 0
while True:
    size = randint(20,100)
    points = randint(2,5) *2+1
    color = (random(),random(),random())
    x = randint(-350,300)
    y = randint(-250,250)
    t.Screen().bgcolor("black")
    if count == 10:
        t.penup()
        t.color("white")
        t.goto(350,220)
        t.pendown()
        t.begin_fill()
        t.circle(50)
        t.end_fill()
    count = count+1
    draw_star(size, points, color, x, y)