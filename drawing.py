from turtle import *

def draw_Calabash():
    # from turtle import *
    bgcolor("sky blue")
    color("chartreuse2")
    pensize(4)
    circle(75,180)
    start_position = position()
    start_heading =  heading()
    left(180)
    circle(30,200)
    penup()  
    goto(start_position) 
    setheading(start_heading)  
    pendown()  

    circle(75,180)
    left(180)
    circle(100,360)
    exitonclick()  


print("----- Welcome to the drawing system ----")
while True:  
            draw_Calabash()


