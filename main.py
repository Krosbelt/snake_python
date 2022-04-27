from turtle import Screen
from snake import Snake

import time


# crear escenario
screen = Screen() #instanciar el objeto
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Programate snake")

screen.tracer(0) #quitamos animación del escenario

#Instanciar (crear) el objeto serpiente
snake = Snake()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.2)

    #Método de movimiento de la serpiente
    snake.move()
    # for segment in segments:
    #     segment.forward(20)
    #     segment[0].left(90)

#Final
screen.exitonclick()