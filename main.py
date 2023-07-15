import random
from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
pos = -100
turtle_list = []
is_on_race = False
for color in colors:
    color_turtle = Turtle(shape="turtle")
    color_turtle.color(color)
    color_turtle.penup()
    color_turtle.goto(x=-230, y=pos)
    pos += 30
    turtle_list.append(color_turtle)

if user_bet:
    is_on_race = True

while is_on_race:
    for turtle in turtle_list:

        if turtle.xcor() > 230:
            is_on_race = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You've won! The {winner} turtle is the winner")
            else:
                print(f"You've lost! The {winner} turtle is the winner")
        turtle.forward(random.randint(0, 10))


screen.exitonclick()
