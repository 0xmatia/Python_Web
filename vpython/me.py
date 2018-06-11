from vpython import *

box(pos=vector(0, 0, 0), length=10, height=0.5, width=10, color=color.blue)

ball = sphere(pos=vector(0, 1, 0), radius=1, color=color.red)
dt = 0.01
while True:
    vec = input("Enter x, y ")
    vec = vec.split(",")
    ball.velocity = vector(int(vec[0]), 0, int(vec[1]))
    rate(100)
    ball.pos = ball.pos + ball.velocity * dt
