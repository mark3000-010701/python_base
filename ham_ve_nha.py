import turtle as t
def draw_rectangle(chieudai,chieurong,mau):
        t.begin_fill()
        t.fillcolor(mau)
        for i in range(2):
                t.forward(chieudai)
                t.left(90)
                t.forward(chieurong)
                t.left(90)

        t.end_fill()

t.speed(100)
t.up()
t.goto(0,-100)
t.down()
draw_rectangle(100,150,'#666666')

t.up()
t.goto(30,-100)
t.down()
draw_rectangle(20,70,'#339900')

t.up()
t.goto(50,-100)
t.down()
draw_rectangle(20,70,'#339900')

t.up()
t.goto(-200,-100)
t.down()
draw_rectangle(200,300,'#CC6666')

t.up()
t.goto(-100,-100)
t.down()
draw_rectangle(100,150,'#CC6666')

t.up()
t.goto(-200,-100)
t.down()
draw_rectangle(100,150,'#CC6666')

t.up()
t.goto(-200,50)
t.down()
draw_rectangle(100,150,'#CC6666')

t.up()
t.goto(-160,-45)
t.down()
draw_rectangle(20,50,'#DDDDDD')

t.up()
t.goto(-160,90)
t.down()
draw_rectangle(20,50,'#DDDDDD')

t.up()
t.goto(-60,-45)
t.down()
draw_rectangle(20,50,'#DDDDDD')

t.up()
t.goto(-60,90)
t.down()
draw_rectangle(20,50,'#DDDDDD')

t.mainloop()
