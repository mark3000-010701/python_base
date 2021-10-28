import turtle as t
import random as r

'''
#vẽ rùa chạy đứt quãng
t.shape("turtle")
t.hideturtle()
t.pensize(3)
t.color("blue")
t.speed(1)
t.penup()
t.goto(-400,0)
t.showturtle()

count=0
while count<10:
    down=r.randint(20,50)
    up=r.randint(20,50)
    t.down()

    t.forward(down)
    t.up()

    t.forward(up)
    count+=1
t.done()
'''
'''
## vẽ rùa chạy trong vòng tròn

#vẽ hình tròn
t.hideturtle()
t.up()
t.goto(0,-200)
t.speed(10)
t.pensize(10)
t.pencolor("black")
t.down()
t.circle(200)
#đặt rùa ở giữa
t.up()
t.speed(10)
t.shape("turtle")
t.pencolor('green')
t.goto(0,0)
'''
# tạo hướng cho rùa
# angle=r.randint(0,360)
# t.right(angle)
# t.showturtle()
'''
#cho rùa thoát khỏi vòng tròn
count=0
while True:
    t.speed(1)
    t.forward(188)
    t.hideturtle()
    t.speed(10)
    t.goto(0,0)
    angle=r.randint(0,360)
    t.right(angle)
    t.showturtle()
    count+=1
    if count==10:
        break
t.done()
'''
'''
import math
d = int(input())
while True:

    t.speed(10)
    t.forward(d)
    t.left(math.pi)
    #t.right(90)
    d+=4
    if t.distance(0,0)>d:
        break
t.done()
'''
'''
#### vẽ xoắn ốc
d=int(input())
t.left(90)
while t.distance(0,0)<1000:
    t.circle(d,100)
    d+=5
t.done
t.mainloop()
'''


### vẽ hình elip và các elip lồng nhau
col=['violet','blue','green','yellow',
     'orange','red']
r=70
val=10
i=0
t.speed(100)
while True:
    t.seth(-val)
    # chọn màu cho elip
    t.color(col[i])
    if i==5:
        i=0
    else:
        i+=1
    ## vẽ elip
    for k in range(2):
        t.circle(r,90)
        t.circle(r/2,90)
    val+=10

t.mainloop()
