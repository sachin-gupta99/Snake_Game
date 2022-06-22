import turtle
FONT = ('Times New Roman', 15, 'bold')
ALIGN = "center"


class Scoreboard(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.pu()
        self.hideturtle()
        self.color("black")
        self.setposition((0, 270))
        self.high_score = 0
        self.read_high_score()
        self.write_score()

    def read_high_score(self):
        try:
            with open('high_score.txt', 'r') as f:
                txt = f.read()
        except FileNotFoundError:
            with open('high_score.txt', 'w') as f:
                f.write("0")
                self.high_score = 0
        else:
            self.high_score = txt

    def write_score(self):
        self.clear()
        self.write(f"Score : {self.score}\t\t High Score : {self.high_score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto((0,0))
        self.clear()
        self.write(f"Game Over", align=ALIGN, font=FONT)

        if int(self.high_score) < self.score:
            with open('high_score.txt', 'w') as f:
                f.write(str(self.score))
            self.high_score = self.score

        self.goto((0, -20))
        self.write(f"Your Score : {self.score}", align=ALIGN, font=FONT)
        self.goto((0, -40))
        self.write(f"High Score : {self.high_score}", align=ALIGN, font=FONT)


