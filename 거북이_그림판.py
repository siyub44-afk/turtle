import turtle
import random
#그저그림거북이
rmwjrmfla = turtle.Turtle()
rmwjrmfla.shape('turtle')
#스크린
s = turtle.Screen()
#거북이 색 정하기
color = ['red', 'green', 'blue', 'black']
shape = ['arrow', 'turtle', 'circle', 'square']

wjwkddlqslek = True
tor = 0
rnfrrl=1

def make_red():
    global tor
    rmwjrmfla.pencolor(color[tor % 4])
    tor += 1

    
#거북이 움직임 수치
def dhls():
    rmwjrmfla.setheading(180)
    rmwjrmfla.forward(3.141592)
def dh():
    rmwjrmfla.setheading(0)
    rmwjrmfla.forward(3.141592)
def dnl():
    rmwjrmfla.setheading(90)
    rmwjrmfla.forward(3.141592)
def dkfo():
    rmwjrmfla.setheading(270)
    rmwjrmfla.forward(3.141592)
#팬 굵기
def ej():
    global rnfrrl
    rnfrrl += 1
    rmwjrmfla.pensize(rnfrrl)
def wjrrp():
    global rnfrrl
    rnfrrl -= 1
    if rnfrrl <= 0:
        rnfrrl=1
    rmwjrmfla.pensize(rnfrrl)

#거북이 클릭 랜덤
def tc(x,y):
    foseja = random.choice(color)
    rmwjrmfla.color(foseja)

    todrlato = random.choice(shape)
    rmwjrmfla.shape(todrlato)
#거북이 팬 업

def vos():
    global wjwkddlqslek

    if wjwkddlqslek:
        rmwjrmfla.penup()
        wjwkddlqslek = False
    else:
        rmwjrmfla.pendown()
        wjwkddlqslek = True

def wldna():
    s.clear()

#거북이 색
s.onkey(make_red,'a')
#키 움직임
s.onkeypress(dkfo,'Down')
s.onkeypress(dhls,'Left')
s.onkeypress(dh,'Right')
s.onkeypress(dnl,'Up')
#거북이 색 랜덤
s.onclick(tc)
#거북이 팬 업
s.onkey(vos,'space')
#굵기
s.onkeypress(ej,'e')
s.onkeypress(wjrrp,'q')
s.onkey(wldna,'r')



s.listen()

turtle.done()
