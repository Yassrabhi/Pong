
import turtle as t
class Ball:
    ball = t.Turtle()
    ball.speed(0)
    ball.shape('circle')
    ball.color('yellow')
    ball.penup()
    ball.goto(0, 0)
    ball_dx = 1.5  # Setting up the pixels for the ball movement.
    ball_dy = 1.5