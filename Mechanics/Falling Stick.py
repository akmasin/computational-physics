from vpython import *

floor = box (pos=vector(0,0,0), length=16, height=0.1, width=16, color=color.blue)
ball = sphere(pos=vector(0,1,0), radius=0.2, color=color.red)
ball2 = sphere(pos=vector(1,1.5,0), radius=0.2, color=color.red)
ball3 = sphere(pos=vector(2,2,0), radius=0.2, color=color.red)
ball4 = sphere(pos=vector(3,2.5,0), radius=0.2, color=color.red)
ball5 = sphere(pos=vector(4,3,0), radius=0.2, color=color.red)
ball6 = sphere(pos=vector(5,3.5,0), radius=0.2, color=color.red)
ball7 = sphere(pos=vector(6,4,0), radius=0.2, color=color.red)
ball8 = sphere(pos=vector(7,4.5,0), radius=0.2, color=color.red)
ball9 = sphere(pos=vector(8,5,0), radius=0.2, color=color.red)
ball10 = sphere(pos=vector(9,5.5,0), radius=0.2, color=color.red)

batang = cylinder(pos=ball.pos,axis=ball2.pos,radius=0.1,color=color.white)
batang2 = cylinder(pos=ball2.pos,axis=ball3.pos,radius=0.1,color=color.white)
batang3 = cylinder(pos=ball3.pos,axis=ball4.pos,radius=0.1,color=color.white)
batang4 = cylinder(pos=ball4.pos,axis=ball5.pos,radius=0.1,color=color.white)
batang5 = cylinder(pos=ball5.pos,axis=ball6.pos,radius=0.1,color=color.white)
batang6 = cylinder(pos=ball6.pos,axis=ball7.pos,radius=0.1,color=color.white)
batang7 = cylinder(pos=ball7.pos,axis=ball8.pos,radius=0.1,color=color.white)
batang8 = cylinder(pos=ball8.pos,axis=ball9.pos,radius=0.1,color=color.white)
batang9 = cylinder(pos=ball9.pos,axis=ball10.pos,radius=0.1,color=color.white)

ball.velocity = vector(0,0,0)
ball2.velocity = vector(0,0,0)
ball3.velocity = vector(0,0,0)
ball4.velocity = vector(0,0,0)
ball5.velocity = vector(0,0,0)
ball6.velocity = vector(0,0,0)
ball7.velocity = vector(0,0,0)
ball8.velocity = vector(0,0,0)
ball9.velocity = vector(0,0,0)
ball10.velocity = vector(0,0,0)
batang.velocity = vector(0,0,0)
e = 0.7*0.01
dt = 0.01
t = 0
tinggi1 = ball.pos.y
tinggi2 = ball2.pos.y
tinggi3 = ball3.pos.y
tinggi4 = ball4.pos.y
tinggi5 = ball5.pos.y
tinggi6 = ball6.pos.y
tinggi7 = ball7.pos.y
tinggi8 = ball8.pos.y
tinggi9 = ball9.pos.y
tinggi10 = ball10.pos.y

while t<100:
    rate (100)
    ball.velocity.y = ball.velocity.y - 9.8*dt -  e*ball.velocity.y
    ball.pos=ball.pos + ball.velocity*dt
    
    ball2.velocity.y = ball2.velocity.y - 9.8*dt -  e*ball2.velocity.y
    ball2.pos=ball2.pos + ball2.velocity*dt
    
    ball3.velocity.y = ball3.velocity.y - 9.8*dt -  e*ball3.velocity.y
    ball3.pos=ball3.pos + ball3.velocity*dt
    
    ball4.velocity.y = ball4.velocity.y - 9.8*dt -  e*ball4.velocity.y
    ball4.pos=ball4.pos + ball4.velocity*dt
    
    ball5.velocity.y = ball5.velocity.y - 9.8*dt -  e*ball5.velocity.y
    ball5.pos=ball5.pos + ball5.velocity*dt
    
    ball6.velocity.y = ball6.velocity.y - 9.8*dt -  e*ball6.velocity.y
    ball6.pos=ball6.pos + ball6.velocity*dt
    
    ball7.velocity.y = ball7.velocity.y - 9.8*dt -  e*ball7.velocity.y
    ball7.pos=ball7.pos + ball7.velocity*dt
    
    ball8.velocity.y = ball8.velocity.y - 9.8*dt -  e*ball8.velocity.y
    ball8.pos=ball8.pos + ball8.velocity*dt
    
    ball9.velocity.y = ball9.velocity.y - 9.8*dt -  e*ball9.velocity.y
    ball9.pos=ball9.pos + ball9.velocity*dt
    
    ball10.velocity.y = ball10.velocity.y - 9.8*dt -  e*ball10.velocity.y
    ball10.pos=ball10.pos + ball10.velocity*dt
    
    batang.pos=ball.pos
    batang.axis = ball2.pos - batang.pos
    batang2.pos=ball2.pos
    batang2.axis = ball3.pos - batang2.pos
    batang3.pos=ball3.pos
    batang3.axis = ball4.pos - batang3.pos
    batang4.pos=ball4.pos
    batang4.axis = ball5.pos - batang4.pos
    batang5.pos=ball5.pos
    batang5.axis = ball6.pos - batang5.pos
    batang6.pos=ball6.pos
    batang6.axis = ball7.pos - batang6.pos
    batang7.pos=ball7.pos
    batang7.axis = ball8.pos - batang7.pos
    batang8.pos=ball8.pos
    batang8.axis = ball9.pos - batang8.pos
    batang9.pos=ball9.pos
    batang9.axis = ball10.pos - batang9.pos
    t = t+dt
    
    if ball.pos.y>tinggi1:
        tinggi1=ball.pos.y
    if ball.pos.y<=ball.radius and ball.velocity.y<0:
        ball.velocity.y = -ball.velocity.y
    if ball2.pos.y>tinggi2:
        tinggi2=ball2.pos.y
    if ball2.pos.y<=ball2.radius and ball2.velocity.y<0:
        ball2.velocity.y = -ball2.velocity.y
    if ball3.pos.y>tinggi3:
        tingg31=ball3.pos.y
    if ball3.pos.y<=ball3.radius and ball3.velocity.y<0:
        ball3.velocity.y = -ball3.velocity.y
    if ball4.pos.y>tinggi4:
        tinggi4=ball4.pos.y
    if ball4.pos.y<=ball4.radius and ball4.velocity.y<0:
        ball4.velocity.y = -ball4.velocity.y
    if ball5.pos.y>tinggi5:
        tinggi5=ball5.pos.y
    if ball5.pos.y<=ball5.radius and ball5.velocity.y<0:
        ball5.velocity.y = -ball5.velocity.y
    if ball6.pos.y>tinggi6:
        tinggi6=ball6.pos.y
    if ball6.pos.y<=ball6.radius and ball6.velocity.y<0:
        ball6.velocity.y = -ball6.velocity.y
    if ball7.pos.y>tinggi7:
        tinggi7=ball7.pos.y
    if ball7.pos.y<=ball7.radius and ball7.velocity.y<0:
        ball7.velocity.y = -ball7.velocity.y
    if ball8.pos.y>tinggi8:
        tinggi8=ball8.pos.y
    if ball8.pos.y<=ball8.radius and ball8.velocity.y<0:
        ball8.velocity.y = -ball8.velocity.y
    if ball9.pos.y>tinggi9:
        tinggi9=ball9.pos.y
    if ball9.pos.y<=ball9.radius and ball9.velocity.y<0:
        ball9.velocity.y = -ball9.velocity.y
    if ball10.pos.y>tinggi10:
        tinggi10=ball10.pos.y
    if ball10.pos.y<=ball10.radius and ball10.velocity.y<0:
        ball10.velocity.y = -ball10.velocity.y
    
    #ball.pos = ball.pos + ball.velocity*dt
    #ball2.pos = ball2.pos + ball2.velocity*dt
    #batang.pos = ball.pos + ball.velocity*dt
    #batang.axis=ball2.pos - batang.pos #+ batang.velocity*dt
    #if ball.pos.y < ball.radius:
    #    ball.velocity.y = abs(ball.velocity.y) - 9.8*dt
    #if ball.pos.y > ball.radius:
    #    ball.velocity.y = ball.velocity.y - 9.8*dt
    #if ball2.pos.y < ball2.radius:
    #    ball2.velocity.y = abs(ball2.velocity.y) - 9.8*dt
    #if ball2.pos.y > ball2.radius:
    #    ball2.velocity.y = ball2.velocity.y - 9.8*dt
    #if ball.velocity.y == 0:
        
        