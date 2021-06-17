import turtle
import random
import time


screen = turtle.Screen()
road_pen = turtle.Turtle()

oppCar1 = road_pen.clone()
oppCar1.penup()
oppCar1.shape("turtle")


xCoor = [0, 58, 116]

oppColours = ['red', 'green', 'yellow']

def spawn(x):
    start = time.time()
    newColour = random.choice(oppColours)
    oppCar1.setposition(x, 250)
    oppCar1.setheading(-90)
    oppCar1.color(newColour)
    newX = random.choice(xCoor)
    while True:
        if time.time() - start > 2:
            print(newX)
            spawn(newX)
            



start = time.time()


spawn(random.choice(xCoor))

screen.exitonclick()