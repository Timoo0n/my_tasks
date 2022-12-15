from turtle import *

def f():
    tracer(0)
    screensize(1000, 1000)
    scale = 25
    for _ in range(7):
        rt(90)
        fd(4*scale)
        for _ in range(2):
            lt(90)
            fd(4*scale)
    up()
    for x in range(-20, 20):
        for y in range(-20, 20):
            goto(x*scale, y*scale)
            dot(3, 'blue')
    update()
    exitonclick()
    

if __name__ == '__main__': f()
