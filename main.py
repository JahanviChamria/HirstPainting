import colorgram
from turtle import Turtle, Screen
import random
turtle=Turtle()
tim=Turtle()
screen=Screen()
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     rgb_colors.append(color.rgb)
#
# print(rgb_colors)
tim.speed("fastest")
screen.colormode(255)
color_list=[(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tim.penup()
tim.hideturtle()
l=len(color_list)
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
for r in range(1, 101):
    ch=random.choice(color_list)
    tim.dot(20, ch)
    tim.forward(50)
    if r%10==0:
        tim.setheading(90)
        tim.penup()
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)




screen.exitonclick()