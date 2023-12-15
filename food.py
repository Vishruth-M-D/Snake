from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("#00ff00")
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.new_food()


    def new_food(self):
        randx = random.randint(-280, 280)
        randy = random.randint(-330, 330)
        self.goto(randx, randy)

