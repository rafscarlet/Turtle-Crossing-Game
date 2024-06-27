from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.move_dist = STARTING_MOVE_DISTANCE
        self.cars = []
        
    def gen_car(self):
        # random_chance = random.randint(1,6)
        # if random_chance==1                    #--- Make this happen approx 1/6 six times
        car = Turtle(shape="square")
        car.penup()
        car.shapesize(stretch_len=2, stretch_wid=1)
        car.color(random.choice(COLORS))
        car.speed(0)
        car.goto(x=300, y=random.randint(-250, 250))
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.goto(car.xcor() - self.move_dist, car.ycor())

    def incr_dist(self):
        self.move_dist += MOVE_INCREMENT
    
        
