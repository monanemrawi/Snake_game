from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", move=False, align="center", font=("Courier", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))
        self.goto(0, -30)
        self.write("Press 'space' to restart game", align="center", font=("Courier", 18, "normal"))

    def reset(self):
        self.clear() 
        self.score = 0
        self.goto(0, 260) 
        self.update_scoreboard()
