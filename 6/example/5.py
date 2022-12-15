from turtle import *


def f():
    screensize(10000, 10000)
    tracer(0)
    r = 25

    for i in range(7):
        goto(xcor() + 6 * r, ycor() - 9 * r)
        goto(xcor() - 6 * r, ycor() + 2 * r)
        goto(xcor() + 12 * r, ycor() + 3 * r)

    up()
    for x in range(-20, 20):
        for y in range(-20, 20):
            goto(x*r, y*r)
            dot(3, 'blue')
    update()


if __name__ == '__main__': f()
