from turtle import Turtle,Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title='Make bet', prompt="Which turtle will win the race? Enter a color: ")
colors = ['red','orange','yellow','green','blue','purple']
y_positions = [-70,-40,-10,20,50,80]
all_turtles = []

for turtle_index in range(6):
    new_turtle = Turtle()
    new_turtle.shape('turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-230, y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet in colors:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            if user_bet == turtle.pencolor():
                print("Congratulations your turtle won!")
            else:
                print(f"Sorry but {turtle.pencolor().capitalize()} turtle won.")


        random_distance = random.randint(0,10)
        turtle.forward(random_distance)




