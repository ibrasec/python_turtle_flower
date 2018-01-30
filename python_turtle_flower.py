#!/usr/bin/python
# done by Ibrahim Abdulghni khorwat
# feel free to change the code

import turtle
def draw():
        w = turtle.Screen()
        w.bgcolor("#ADEAEA")
        t = turtle.Turtle()
        t.ht(); t.speed(100)
        color_list = ["#FF82AB","#EE1289","#FF82AB","#FFB6C1"]
        t.shape('circle')
        # To have 4 different colors
        for i in range(4):
                # to change the pen size for each color
                t.pensize(20-i*4.75) ; t.color(color_list[i])
                for j in range(12):
                    for k in range(4):
                        t.forward(120)
                        t.right(120)
                    t.right(30)
        t.color("#EE1289");t.pensize(1)
        t.setpos(-250,0)
        t.write("Udacity-flower", True, font=("Andale Mono", 20, "normal"))
        w.exitonclick()
        

draw()

