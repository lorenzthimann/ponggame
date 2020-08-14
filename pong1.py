# count marks and go faster as the game goes
import turtle
import time
import random


points_a = 0
points_b = 0
not_first_time = False
wn = turtle.Screen()
wn.title("Pong game from Lorenz")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


paddle_a = turtle.Turtle()
paddle_a.penup()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.goto(-350, 0)
paddle_a.shapesize(stretch_wid= 4, stretch_len = 1)

paddle_b = turtle.Turtle()
paddle_b.penup()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.goto(350, 0)
paddle_b.shapesize(stretch_wid= 4, stretch_len = 1)

ball = turtle.Turtle()
ball.penup()
ball.shape("circle")
ball.color("white")
ball.goto(0, 0)
ball.speed(0)

def paddle_a_up():
    y = paddle_a.ycor()
    paddle_a.sety(y+ 80)

def paddle_a_down():
    y = paddle_a.ycor()
    paddle_a.sety(y - 40)
def paddle_b_up():
    y = paddle_b.ycor()
    paddle_b.sety(y+ 80)
def paddle_b_down():
    y = paddle_b.ycor()
    paddle_b.sety(y - 40)

def keyboard_input():
    turtle.listen()
    turtle.onkey(paddle_a_up, "q")
    turtle.onkey(paddle_a_down, "a")
    turtle.onkey(paddle_b_up, "Up")
    turtle.onkey(paddle_b_down, "Down")

def draw_score():
    global pen
    pen = turtle.Turtle()
    pen.clear()
    pen.speed(0)
    pen.color("white")
    pen.hideturtle()
    pen.penup()
    pen.goto(0, 260)
    pen.write(f"Player A : {points_a} Player B : {points_b}", align="center", font= ("courier", 24, "normal"))
draw_score()
def ball_moving():
    # if touches paddle n( and b should touch matches), gain pt, vary and varx *= 1.1, change b should touch, adjust points
    global b_should_touch
    global not_first_time
    global variation_of_y
    global variation_of_x
    global points_a
    global points_b
    global touched_top
    global touched_bottom
    global last_time_it_has_touched

    last_time_it_has_touched = 0
    
    if not not_first_time:
        variation_of_y = 0.01
        variation_of_x = 0.2
        b_should_touch = True
        points_a = 0
        points_b = 0
        touched_top = False
        touched_bottom = True
    x = ball.xcor()
    y = ball.ycor()
    # move the ball
    ball.goto(x + variation_of_x, y + variation_of_y)
    time_now = time.time()
    if y > 290: # touches top
        ball.sety(y - 10)
        variation_of_y *= -1
    if y < -290: # touches bottom
        ball.sety(y + 10)
        variation_of_y *= -1
    # check if out on left or right side
    if x > 400:
        points_a += 1
        ball.goto(0, 0)
        variation_of_x *= 0.9
        time.sleep(1)
        pen.clear()
        draw_score()
    if x < -400:
        points_b += 1
        ball.goto(0, 0)
        variation_of_y = 0.01
        variation_of_x = 0.2
        time.sleep(1)
        pen.clear()
        draw_score()
    # check if touches paddle 
    if paddle_b.distance(ball) < 40:
        ball.setx(x - 2)
        variation_of_x = variation_of_x * -1.05
        variation_of_y = variation_of_y * (random.randint(8, 50) / 10)
    if paddle_a.distance(ball) < 40:
        ball.setx(x + 2)
        variation_of_x = variation_of_x * -1.05




    not_first_time = True
    
   
while True: 
    
    wn.update()
    ball_moving()
    keyboard_input()
    

