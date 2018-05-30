from vpython import *

box(pos=vector(0, 0, 0), length=10, height=0.5, width=10, color=color.blue)

ball = sphere(pos=vector(0, 10, 0), radius=1, color=color.red)
ball.velocity = vector(1, -2, 0)
dt = 0.01
while True:
    rate(100)
    ball.pos = ball.pos + ball.velocity * dt
    if ball.pos.y < ball.radius:
        ball.velocity.y = abs(ball.velocity.y)
    else:
        ball.velocity.y = ball.velocity.y - 9.8*dt
