import turtle
import random

turtle.title("My Turtle Game")
turtle.bgcolor("black")
turtle.setup(600, 600)

screen = turtle.Screen() 
terry = turtle.Turtle() 
terry.color("blue")
terry.speed(0)
terry.pensize(3)
terry.shape("turtle")
sides = 5

def spiral(angle, increase):
  steps = 5
  for i in range(500):
    # if i == 250:
    #   terry.color("purple")
    colors = ["maroon", "navy blue"]
    terry.color(random.choice(colors))
    terry.forward(steps)
    terry.left(angle)
    steps += increase

spiral(angle = 360/sides+1, increase=1)
