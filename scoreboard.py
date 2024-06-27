from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.penup()
        self.color("black")
        self.goto(-270, 250)
        self.score = 0
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write(arg=f"Level: {self.score}", font=FONT)

    def incr_score(self):
        self.score += 1

    def game_over(self):
        self.home()
        self.write(arg="GAME OVER", align="center", font=FONT)