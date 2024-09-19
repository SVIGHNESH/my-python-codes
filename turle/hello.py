from turtle import *
import colorsys

# Set up the screen size
setup(width=800, height=600)
bgcolor('black')


tracer(500)

def draw():
    h = 0
    for i in range(100):
        c = colorsys.hsv_to_rgb(h, 1, 1)
        h += 0.01
        up()
        goto(-3, 2 - i * 4)  # Adjust these values as needed
        down()
        color('black')
        fillcolor(c)
        begin_fill()
        rt(98)
        circle(i, 12)
        fd(290)
        fd(i)
        lt(29)
        for j in range(129):
            fd(i)
            circle(j, 299, steps=2)
        end_fill()
    update()

draw()
done()
