import turtle as t
import random as r
import datetime

screen = t.Screen()
screen.setup(height=500, width=600)
t.Turtle(visible=False)
t.up()
t.speed(0)
t.goto(-250, 200)
for i in range(21):
    t.write(i)
    t.forward(25)
x = -250
t.goto(-250, 200)
t.right(90)
for i in range(21):
    for j in range(10):
        t.down()
        t.forward(20)
        t.up()
        t.forward(10)
    t.up()
    t.forward(5)
    t.write(i)
    t.goto(x + (i + 1) * 25, 200)
all_turtle = []
y = [160, 100, 40, -20, -80]
colors = ['red', 'green', 'blue', 'yellow', 'black']
for i in range(0, 5):
    p = t.Turtle(shape="turtle")
    p.penup()
    p.goto(x=-250, y=y[i])
    p.color(colors[i])
    for j in range(5):
        p.left(72)
    all_turtle.append(p)

'''
def random_walk(turtles):
    global run
    for turtle in turtles:
        turtle.forward(r.randint(1, 10))
        if turtle.xcor() > 250:
            win=turtle
            run = False
    #print("thắng")
            # print(f"rùa {all_turtle[colors[run]]} thắng")

'''
run = True
while run:
    #random_walk(all_turtle)
    #global run
    for turtle in range(0,len(colors)):
        timestart = datetime.datetime.now()
        all_turtle[turtle].forward(r.randint(1, 10))
        if all_turtle[turtle].xcor() > 250:
            win = turtle
            timeend=datetime.datetime.now()
            run = False

#t.write(f"turtle {colors[win]} is winner",align="left")
t.write(f" turtle {colors[win]} is winner run time: {timeend-timestart}",align="left")
screen.exitonclick()
t.mainloop()

'''
a=[]
while len(a)==0:
    for i in range(5):
        i = int(input())
        a.append(i)
a.sort()
if len(a)<2:
    print(a)
else:
    print(a[-1],a[-2])
'''
