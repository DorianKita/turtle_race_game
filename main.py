from turtle import Turtle,Screen

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title='Make bet', prompt="Which turtle will win the race? Enter a color: ")
colors = ['red','orange','yellow','green','blue','purple']
y = -120

for color in colors:
    tim = Turtle()
    tim.shape('turtle')
    tim.color(color)
    tim.penup()
    tim.goto(-230,y)
    y += 50


screen.exitonclick()