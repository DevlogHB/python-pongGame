from turtle import Turtle;

# Turtle 클래스 상속 받은 Ball 클래스
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white");
        self.shape("circle");
        self.penup();
        self.x_move = 10;
        self.y_move = 10;
        self.move_speed = 0.1;
    
    def move(self):
        new_x = self.xcor() +self.x_move;
        new_y = self.ycor() +self.y_move;
        self.goto(new_x, new_y);

    # 좌표가 + or - 인 상태에서 부딪히는 경우 부호(- or +) 변경
    def bounceY(self):
        self.y_move *= -1;

    def bounceX(self):
        self.x_move *= -1;
        self.move_speed *= 0.9;

    def reset_position(self):
        self.goto(0,0);
        self.move_speed = 0.1;
        self.bounceX();
        
        