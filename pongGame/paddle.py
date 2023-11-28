from turtle import Turtle;

# Turtle 클래스 상속 받은 Paddle 클래스
class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.new_x = x;
        self.new_y = y;
        self.shape("square");
        self.color("white");
        self.shapesize(5,1);
        self.penup();
        self.goto(self.new_x, self.new_y);

    def move_up(self):
        new_y = self.ycor() + 20;
        self.goto(self.xcor(), new_y);

    def move_down(self):
        new_y = self.ycor() - 20;
        self.goto(self.xcor(), new_y);