from turtle import Screen;
from paddle import Paddle;
from ball   import  Ball;
from scoreboard import Scoreboard;
import time;

screen = Screen();
screen.bgcolor("black");
screen.setup(800, 600);
screen.title("Pong Game");
screen.tracer(0);

right_paddle = Paddle(350,0);
left_paddle = Paddle(-350,0);
ball = Ball();
scoreboard = Scoreboard();

# 왼, 오른쪽 paddle 키 설정
screen.listen();
screen.onkey(right_paddle.move_up,"Up");
screen.onkey(right_paddle.move_down,"Down");
screen.onkey(left_paddle.move_up,"w");
screen.onkey(left_paddle.move_down,"s");

is_game = True;
while is_game:
    time.sleep(ball.move_speed);
    screen.update();
    ball.move();
    scoreboard;
    # 상/하 충돌 감지
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounceY();

    # 오른쪽, 왼쪽 paddle과 ball 충돌 감지
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.bounceX();

    # 오른쪽 paddle 공 놓침
    if ball.xcor() > 380:
        ball.reset_position();
        scoreboard.left_point();
    
    # 왼쪽 paddle 공 놓침
    if ball.xcor() <-380:
        ball.reset_position();
        scoreboard.right_point();


screen.exitonclick();