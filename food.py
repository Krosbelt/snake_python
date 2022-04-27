from re import X
from turtle import Turtle

#Generar la comida aleatoria
import random

class Food(Turtle):

    def __init__(self):
        super().__init__() #indica que herede todo
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("white")
        self.refresh()

    #Movimiento de food 
    def refresh(self):
        random_x = random.randint(-200, 200)
        random_y = random.randint(-200, 200)
        self.goto(random_x, random_y)