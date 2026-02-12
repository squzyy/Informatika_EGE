'''
from turtle import *
k = 33
tracer(0)
screensize(2000,2000)
left(90)

for i in range(2):
    forward(13 * k)
    right(90)
    forward(20 * k)
    right(90)
up()
fd(8 * k)
rt(90)
back(3 * k)
left(90)
down()
for i in range(2):
    forward(16 * k)
    right(90)
    forward(8 * k)
    right(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * k, y * k)
        dot(3, 'red')
done()


from turtle import *
k = 35
tracer(0)
left(90)
screensize(2000,2000)

for i in range(4):
    fd(10 * k)
    rt(90)
up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * k, y * k)
        dot(13, 'red')
done()


from turtle import *
k = 35
left(90)
tracer(0)
screensize(2000,2000)


for i in range(2):
    forward(10 * k)
    rt(90)
    fd(18 * k)
    rt(90)
up()

fd(5 * k)
rt(90)
fd(7 * k)
lt(90)
down()

for i in range(2):
    fd(10 * k)
    rt(90)
    fd(7 * k)
    rt(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * k, y * k)
        dot(5, 'red')
done()


from turtle import *
k = 15
lt(90)
tracer(0)
screensize(20000, 20000)

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

for x in range(-150, 150):
    for y in range(-150, 150):
        dot(5, 'red')
        goto(x * k, y *k)
done()

from turtle import *
k = 30
lt(90)
tracer(0)
screensize(2000,2000)

for i in range(4):
    fd(6 * k)
    rt(150)
    fd(6 * k)
    rt(30)
up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * k, y * k)
        dot(5, 'red')
done()
'''
'''
from turtle import *
tracer(0)
lt(90)
k = 35
screensize(2000, 2000)

for i in range(5):
    fd(20 * k)
    rt(90)
    fd(3 * k)
up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * k, y * k)
        dot(3, 'red')
done()
'''
'''
from turtle import*

left(90)
tracer(0)
screensize(2000, 2000)
k = 15

for i in range(7):
    fd(10 * k)
    rt(120)
up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * k, y * k)
        dot(3, 'red')
done()
'''

from turtle import*
k = 15
left(90)
screensize(2000, 2000)
tracer(0)

for i in range(2):
    fd(3 * k)
    rt(90)
    fd(20 * k)
    rt(90)
up()
bk(8 * k)
rt(90)
fd(9 * k)
lt(90)
down()

for i in range(2):
    fd(16 * k)
    rt(90)
    fd(8 * k)
    rt(90)
up()

for x in range(-50, 50):
    for y in range(-50, 50):
        dot(3, 'red')
        goto(x * k, y * k)
done()