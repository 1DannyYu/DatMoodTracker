import turtle

# Window setup
win = turtle.Screen()
win.title("Pong in Python")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Left paddle
left = turtle.Turtle()
left.speed(0)
left.shape("square")
left.color("white")
left.shapesize(stretch_wid=5, stretch_len=1)
left.penup()
left.goto(-350, 0)

# Right paddle
right = turtle.Turtle()
right.speed(0)
right.shape("square")
right.color("white")
right.shapesize(stretch_wid=5, stretch_len=1)
right.penup()
right.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.25
ball.dy = 0.25

# Score
score_left = 0
score_right = 0

score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("0 : 0", align="center", font=("Courier", 24, "normal"))

# Paddle movement
def left_up():
    y = left.ycor()
    if y < 250:
        left.sety(y + 20)

def left_down():
    y = left.ycor()
    if y > -250:
        left.sety(y - 20)

def right_up():
    y = right.ycor()
    if y < 250:
        right.sety(y + 20)

def right_down():
    y = right.ycor()
    if y > -250:
        right.sety(y - 20)

# Keyboard bindings
win.listen()
win.onkeypress(left_up, "w")
win.onkeypress(left_down, "s")
win.onkeypress(right_up, "Up")
win.onkeypress(right_down, "Down")

# Main loop
while True:
    win.update()

    # Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # --- AI PADDLE LOGIC HERE ---
    if right.ycor() < ball.ycor() and abs(right.ycor() - ball.ycor()) > 10:
        right.sety(right.ycor() + 0.25)
    elif right.ycor() > ball.ycor() and abs(right.ycor() - ball.ycor()) > 10:
        right.sety(right.ycor() - 0.25)


    # Border bounce
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Right wall
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_left += 1
        score_display.clear()
        score_display.write(f"{score_left} : {score_right}", align="center", font=("Courier", 24, "normal"))

    # Left wall
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_right += 1
        score_display.clear()
        score_display.write(f"{score_left} : {score_right}", align="center", font=("Courier", 24, "normal"))

    # Paddle collisions
    if (340 < ball.xcor() < 350) and (right.ycor() - 50 < ball.ycor() < right.ycor() + 50):
        ball.setx(340)
        ball.dx *= -1

    if (-350 < ball.xcor() < -340) and (left.ycor() - 50 < ball.ycor() < left.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -1
