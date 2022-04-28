from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# crear escenario
screen = Screen()  # instanciar el objeto
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Programate snake")

screen.tracer(0)

#instanciar(crear) el objeto serpiente
snake = Snake()

#instanciar el objeto food
food = Food()

#instanciar el objeto tablero de puntos
Scoreboard = Scoreboard()

#movimientos snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.2)

    snake.move()

    #detectar la colisión con la food
    if snake.head.distance(food) < 15:
        food.refresh()
        Scoreboard.increase_score()
        snake.extend()

    #detectar colisión con los bordes
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        Scoreboard.game_over()  

    #detectar la colision de la cola
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            Scoreboard.game_over()    

screen.exitonclick()