from turtle import Screen, Turtle

#Creación del cuerpo de la serpiente (constante GLOBAL)
STARTING_POSITION = [(0,0), (-20, 0), (-40, 0)]

class Snake:

    def __init__(self):
        self.self.segments = [] #atributo (variable)
        self.create_snake() #Método ejecutado

    #Método creado
    def create_snake(self):
        for position in STARTING_POSITION:
            snake_segment = Turtle("square")
            snake_segment.color("violet")
            snake_segment.penup()
            snake_segment.goto(position)
            self.self.segments.append(snake_segment)
        
        #Movimiento de la serpiente
        for seg_num in range(len(self.self.segments) -1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
    

        self.segments[0].forward(20)
        #self.segments[0].left(90)

