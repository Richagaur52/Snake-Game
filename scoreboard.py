from turtle import Turtle
alignment="center"
Font=("Arial",20,"normal")
class Score(Turtle):
    def __init__(self):
        super(Score, self).__init__()
        self.score=0
        with open("data.txt",mode="r") as data:
            data_h=int(data.read())
            self.high_score=data_h
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.score_update()

    def score_update(self):
        self.clear()
        self.write(f"SCORE:{self.score} HIGH_SCORE:{self.high_score}",align=alignment,font=Font)


    def high_score_increase(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")

        self.score=0
        self.score_update()

    def score_increase(self):
        self.score+=1
        self.score_update()


