import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("LightBlue2")
screen.tracer(0)

timmy = Player()
score = Scoreboard()
car_manager = CarManager()

# Bind the Up key to move the player
screen.listen()
screen.onkeypress(fun=timmy.move, key="Up")

i = 1
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_cars()
    i += 1
    
    # Generate a new car only every 6th time the loops runs (0.6 seconds)
    if i % 6 == 0:
        car_manager.gen_car()
    
    # Reach the top of the screen
    if timmy.ycor() >= 280:
        timmy.pass_level()
        score.incr_score()
        score.update_score()
        car_manager.incr_dist()
    
    # Collision with a car
    for car in car_manager.cars:
        if car.distance(timmy) < 20:
            game_is_on = False
            score.game_over()

screen.exitonclick()
