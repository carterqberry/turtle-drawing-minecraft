'''
Project Name: Turtle Patterns 1
Author: Carter Quesenberry
Due Date: 09-16-2022
Course: CS1400-X01

Using the turtle library, this program draws a picture of a minecraft world :)
I left lots of notes so the program is easy to follow.
Set the window width to 700 and the height to 550.
'''

import turtle

def circle(t, radius, fill, color1):
    if color1 != "":
        t.color(color1)
    if fill:
        t.begin_fill() 
    t.circle(radius)
    if fill:
        t.end_fill()
        
        
def square(t, length, fill, color1):
    i = 0
    if color1 != "":
        t.color(color1)
    if fill:
        t.begin_fill() 
    for i in range(2):
        t.forward(length)
        t.left(90)
        t.forward(length)
        t.left(90)
        i = i + 1
    if fill:
        t.end_fill()

def star(t, size, fill, color1):
    i = 0
    if color1 != "":
        t.color(color1)
    if fill:
        t.begin_fill() 
    for i in range(5):
        t.forward(size)
        t.left(216)
        i = i + 1
    if fill:
        t.end_fill()

def draw_tree(t):
    i = 0
    square(t, 50, True, "green")
    t.forward(50)
    square(t, 50, True, "green")
    t.right(90)
    square(t, 50, True, "green")
    t.right(180)
    t.forward(50)
    t.right(90)
    square(t, 50, True, "green")
    t.forward(50)
    t.right(90)
    t.forward(40)
    t.left(90)
    for i in range(2):
        square(t, 30, True, '#654321')
        t.forward(30)
        i = i + 1

def draw_cloud(t):
    i = 0
    for i in range(3):
        square(t, 50, True, "gray")
        t.forward(50)
        i = i + 1

def rectangle(t, length, width, fill, color1):
    i = 0
    if color1 != "":
        t.color(color1)
    if fill:
        t.begin_fill() 
    for i in range(2):
        t.forward(length)
        t.right(90)
        t.forward(width)
        t.right(90)
        i = i + 1
    if fill:
        t.end_fill()

def main():
    try:
        width = int(input("Enter width of window:\n"))
        height = int(input("Enter height of window:\n"))
    except ValueError:
        print('Width and height must be positive integers.')
        return
    if width < 1 or height < 1:
        print('Width and height must be positive integers.')
        return
    
    #finish set up
    t = turtle.Turtle()
    t.shape("turtle")
    turtle.bgcolor("black")
    turtle.setup (width, height)

    #let the drawing begin!   
    #moves turtle to top left of window    
    t.pu()
    t.goto(-170,140)

    #drawing moon
    circle(t,50,True, '#D3D3D3')

    #drawing cloud
    t.pu()
    t.goto(100,100)
    draw_cloud(t)
    t.goto(50,150)
    draw_cloud(t)

    #drawing first tree
    t.pu()
    t.goto(200,-50)
    t.right(90)
    draw_tree(t)

    #drawing second tree
    t.pu()
    t.goto(-50,-50)
    draw_tree(t)

    #drawing third tree
    t.pu()
    t.goto(-250,-50)
    draw_tree(t)

    #draw ground
    t.pu()
    t.goto(-350, -210)
    t.left(90)
    rectangle(t, 700, 10, True, "green")
    t.goto(-350, -220)
    rectangle(t, 700, 55, True, '#654321')

    #draw stars
    t.pu()
    t.goto(-300, 80)
    star(t, 15, True, "white")
    t.goto(-260, 180)
    star(t, 15, True, "white")
    t.goto(-220, 0)
    star(t, 15, True, "white")
    t.goto(-160, -40)
    star(t, 15, True, "white")
    t.goto(-130, 75)
    star(t, 15, True, "white")
    t.goto(0, 180)
    star(t, 15, True, "white")
    t.goto(65, -65)
    star(t, 15, True, "white")
    t.goto(90, 30)
    star(t, 15, True, "white")
    t.goto(160, 80)
    star(t, 15, True, "white")
    t.goto(300, -20)
    star(t, 15, True, "white")
    t.goto(280, 250)
    star(t, 15, True, "white")

    t.goto(70, -210)
    turtle.done()

    
if __name__ == "__main__":
    main()
