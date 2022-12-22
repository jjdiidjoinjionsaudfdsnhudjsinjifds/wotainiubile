import turtle

a = turtle.Turtle()#a是王八
turtle.hideturtle()#隐藏元王八
a.shape('arrow')#设置为丘比特的箭头
a.color('red', 'red')#颜色
a.speed(0)
a.begin_fill()
def circle():#两个圈
    a.circle(50)
    a.back(100)
    a.seth(0)
    a.circle(50)
    

circle()

a.lt(30)
a.fd(50)
a.rt(50)
a.fd(10)
a.bk(30)#小三角
a.home()
a.fd(25)
a.rt(130)
a.fd(100)
a.lt(85)
a.bk(110)
a.end_fill()


#修补
a.seth(90)
a.begin_fill()
a.fd(50)
a.rt(90)
a.fd(150)
a.rt(90)
a.fd(50)
a.rt(90)
a.fd(150)
a.end_fill()
a.color('white')          
a.pu()
a.hideturtle()
a.seth(0)
a.fd(150)
a.pd()
a.dot(15)

turtle.mainloop()