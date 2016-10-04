__author__ = 's41b'
# -*- coding: utf-8 -*-
import turtle
import random
'''
def moveTo(t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def Goto(x,y,t,w):#学姐的程序
    t.penup()
    t.goto(x,y)
    t.pendown()
def goto(t,w,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
def yun():


    t.begin_fill()  # 颜色填充开始
    t.forward(l)
    t.right(30)
    t.forward(l)
    t.right(150)
    t.forward(l)
    t.right(30)
    t.forward(l)
    t.right(150)  # 以上是画叶子的过程
    t.end_fill()
'''
def cheart(t):#想要画心
    t.fillcolor('#edff5b')
    t.begin_fill()
    t.left(130)
    t.forward(20)
    for i in range(31):
        t.right(6)
        t.forward(1)
    t.left(100)
    for i in range(31):
        t.right(6)
        t.forward(1)
    t.forward(20)
    t.end_fill()
def moveTo(t,x,y):#x,y为坐标，移动到xy，
    # 不留下移动的路径，之后会多次用到
    t.penup()
    t.goto(x,y)
    t.pendown()
def cl(qsd=0):
    if qsd==1:
        return 'springgreen'
    else:
        we=[random.random() for i in range(3)]
        return we
def drawleaves(e,wid,t,l):    #画叶子的函数,e:叶子颜色；l：叶子长度
    #可以选择不调用，只需把tree（）里的else去掉就可以了
    t.pensize(wid)#t是海龟；wid是笔的尺寸
    t.color(e)#叶子的颜色：springgreen。春天的绿色
    t.begin_fill()#颜色填充开始
    t.forward(l)
    t.right(30)
    t.forward(l)
    t.right(150)
    t.forward(l)
    t.right(30)
    t.forward(l)
    t.right(150)#以上是画叶子的过程
    t.end_fill()#填充结束
def tscolor(it):  #颜色库，随着每次递归调用，it++，调用不同的颜色，
    # 这些颜色也是有一定变化规律的，我从PS中一个个弄出来的
    colorstore=['#915f38','#dabb5b','#c0c150','#aac154','#aac154','#4edf7e',\
                '#25fa7e','#3efa74','#0ff58a','#09f578','#17f57c']
    return colorstore[it]
def drawsuna(t):
    t.up()
    t.goto(240,250)
    t.right(90)
    #t.down()
    cheart(t)#画心
    t.left(120)
    t.up()
    t.goto(240,260)
    t.down()
    t.begin_fill()
    t.color('#ee2a08')
    t.circle(8)
    t.end_fill()
def tree(e,t,bralen,i=8,k=30,j=0,s=14,q=1.2,rt=10):#t是海龟；br：树干长度；
    # i：树枝粗细；k：倾斜角度（用20~40）;q:树枝每次的递减
    if bralen>6:  #用6做一个结束条件，6可以改
        t.pensize(i)
        t.color(tscolor(j))  #每次调用改变一次颜色
        j+=1  #用来改变树枝颜色
        u=random.randint(-10,10)  #偏角的随机变化
        d=random.randint(2,14)  #树枝长度的变化
        t.forward(bralen+d)
        t.right(k-u)  #通过u实现20~40的偏角
        tree(e,t,bralen-rt,i-q,k,j,s,q,rt)
        t.left(2 * k - 2 * u - 3)
        tree(e,t,bralen-rt,i-q+0.1,k,j,s,q,rt)  #右树枝与左树枝粗一细不同，这些参数可以改
        t.right(k-u-3)
        t.color(tscolor(j-1))
        t.backward(bralen+d)
    else:
        drawleaves(cl(e),i,t,s)  #画叶子，按照题目可以没有
def write(t):  #这一个函数可以没有
    t.up()  #提笔，不能留goto的轨迹
    t.goto(-110,-230)
    t.down()
    t.color('springgreen')
    t.write('He is young but he is daily growing!', \
            font=("MV Boli", 20, "normal"))
def main(): #主函数
    t = turtle.Turtle()
    w = turtle.Screen()
    #turtle.setup(600, 900, 0, 0)  # 设定画布的大小的函数
    t.hideturtle()
    turtle.tracer(0)
    t.speed(10)
    w.title('韦庆朗的分形树之一') #屏幕的题目
    moveTo(t,-180,-240)
    t.left(90)
    tree(0,t,90,11,30)#递归画树
    moveTo(t,-140,-300)
    tree(1,t,60,5,25,1,6,0.7,8)
    #t.up()
    drawsuna(t)
    write(t)#写字，可以没有
    turtle.update()
    w.exitonclick()  #点击结束


main()

