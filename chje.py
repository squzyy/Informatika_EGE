from turtle import *
k = 35
lt(90)
tracer(0)
screensize(2000, 2000)

for i in range(7):
    fd(15 * k)
    rt(90)
    fd(23 * k)
    rt(90)
up()

fd(3 * k)
rt(90)
fd(5 * k)
rt(90)
down()

for i in range(7):
    fd(252 * k)
    rt(90)
    fd(398 * k)
    rt(90)
up()

for x in range(-50, 50):
    for y in range(-50, 50):
        dot(5, 'red')
        goto(x * k, y *k)
down()