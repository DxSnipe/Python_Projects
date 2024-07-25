import colorgram


rgb_colors = []
colors = colorgram.extract('hist.jpg', 12)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_colors = (r, g, b)
    rgb_colors.append(new_colors)

print(rgb_colors)
import random
import turtle
from turtle import Turtle

turtle.colormode(255)
timmy = Turtle()

colors = [(202, 236, 143), (148, 215, 166), (211, 154, 97), (52, 107, 132), (176, 78, 34), (238, 246, 243),
          (200, 142, 33), (116, 155, 171), (124, 79, 98), (122, 175, 157), (229, 197, 128), (231, 238, 242)]

for i in range(10):
    timmy.dot(20, random.choice(colors))
    turtle.forward(50)

turtle.exitonclick()
