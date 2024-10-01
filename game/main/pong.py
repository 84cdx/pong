import turtle
import winsound
import keyboard
import time

wn = turtle.Screen()
wn.title("Pong by cdx")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

start = False


def check_start():
    return start


paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("#fe019a")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a.hideturtle()

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("#fe019a")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.hideturtle()

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("#ffffff")
ball.penup()
ball.goto(0, 0)
ball.dx = 3
ball.dy = 3
ball.hideturtle()

score = int()
pen = turtle.Turtle()
pen.speed(0)
pen.color("#000000")
pen.penup()
pen.hideturtle()
pen.goto(0, 190)


def get_score():
    return score


pen.write(get_score(), align="center", font=("Arial", 48, "bold"))

startText = turtle.Turtle()
startText.speed(0)
startText.color("white")
startText.penup()
startText.goto(0, 0)
startText.write("press Enter to start", align="center", font=("Arial", 18, "bold"))
startText.hideturtle()


def paddle_a_up():
    y = paddle_a.ycor()
    if y < 241:
        y += 16
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    if y > -240:
        y -= 16
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    if y < 241:
        y += 16
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    if y > -240:
        y -= 16
    paddle_b.sety(y)


wn.listen()
wn.onkeypress(paddle_a_up, 'w')
wn.onkeypress(paddle_a_down, 's')
wn.onkeypress(paddle_b_up, 'Up')
wn.onkeypress(paddle_b_down, 'Down')

while True:
    time.sleep(1 / 60)
    wn.update()
    if not check_start():
        keyboard.wait("enter")
        start = True
        startText.hideturtle()
    pen.write(get_score(), align="center", font=("Arial", 48, "bold"))
    startText.clear()
    paddle_a.showturtle()
    paddle_b.showturtle()
    ball.showturtle()
    pen.color("#18191A")

    get_score()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("4388__noisecollector__pongblipe5.wav", winsound.SND_ASYNC)

    if ball.ycor() < -285:
        ball.sety(-285)
        ball.dy *= -1
        winsound.PlaySound("4388__noisecollector__pongblipe5.wav", winsound.SND_ASYNC)

    if ball.xcor() > 383:
        ball.setx(383)
        ball.goto(0, 0)
        ball.dx *= -1
        score = 0
        pen.clear()
        pen.write(get_score(), align="center", font=("Arial", 48, "bold"))

    if ball.xcor() < -390:
        ball.setx(-390)
        ball.goto(0, 0)
        ball.dx *= -1
        score = 0
        pen.clear()
        pen.write(get_score(), align="center", font=("Arial", 48, "bold"))

    if (333 < ball.xcor() < 350) and (
            paddle_b.ycor() + 40 > ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(333)
        ball.dx *= -1
        score += 10
        pen.clear()
        pen.write(get_score(), align="center", font=("Arial", 48, "bold"))
        winsound.PlaySound("4388__noisecollector__pongblipe5.wav", winsound.SND_ASYNC)

    if (-333 > ball.xcor() > -350) and (
            paddle_a.ycor() + 40 > ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-333)
        ball.dx *= -1
        score += 10
        pen.clear()
        pen.write(get_score(), align="center", font=("Arial", 48, "bold"))
        winsound.PlaySound("4388__noisecollector__pongblipe5.wav", winsound.SND_ASYNC)
