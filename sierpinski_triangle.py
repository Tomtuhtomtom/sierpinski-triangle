import turtle
import math
import random

sierpinski = turtle.Turtle()
SLOPE_OF_EQ_TRIANGLE = -1.73205081
triangle_side_length = 500
number_of_dots = 5000

a = [0, math.sqrt((triangle_side_length ** 2)-((triangle_side_length/2) ** 2))/2]
b = [triangle_side_length/2, -math.sqrt((triangle_side_length ** 2)-((triangle_side_length/2) ** 2))/2]
c = [-triangle_side_length/2, -math.sqrt((triangle_side_length ** 2)-((triangle_side_length/2) ** 2))/2]

origin_points = [a, b, c]

random_x_coordinate = random.uniform(-triangle_side_length/2, triangle_side_length/2)
random_y_coordinate = random.uniform(-math.sqrt((triangle_side_length ** 2)-((triangle_side_length/2) ** 2))/2, (SLOPE_OF_EQ_TRIANGLE * abs(random_x_coordinate)) + math.sqrt((triangle_side_length ** 2)-((triangle_side_length/2) ** 2))/2)
random_point = [random_x_coordinate, random_y_coordinate]

def draw_triangle():
    sierpinski.penup()
    sierpinski.setpos(a[0], a[1])
    sierpinski.pendown()
    sierpinski.goto(b[0], b[1])
    sierpinski.goto(c[0], c[1])
    sierpinski.goto(a[0], a[1])
    sierpinski.penup()
    sierpinski.setpos(random_point[0], random_point[1])
    sierpinski.dot()
    i = 0
    while i < number_of_dots:
        p = random.choice(list(origin_points))
        sierpinski.setpos(p[0]-((p[0]-sierpinski.pos()[0])/2), p[1]-((p[1]-sierpinski.pos()[1])/2))
        sierpinski.dot()
        i+=1

draw_triangle()

turtle.done()
