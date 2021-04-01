from vpython import *
from math import sqrt, asin, atan
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

batang = cylinder(pos=ball.pos,axis=ball10.pos-ball.pos,radius=0.1,color=color.white)
#batang2 = cylinder(pos=ball2.pos,axis=ball3.pos-ball2.pos,radius=0.1,color=color.white)
#batang3 = cylinder(pos=ball3.pos,axis=ball4.pos-ball3.pos,radius=0.1,color=color.white)
#batang4 = cylinder(pos=ball4.pos,axis=ball5.pos-ball4.pos,radius=0.1,color=color.white)
#batang5 = cylinder(pos=ball5.pos,axis=ball6.pos-ball5.pos,radius=0.1,color=color.white)
#batang6 = cylinder(pos=ball6.pos,axis=ball7.pos-ball6.pos,radius=0.1,color=color.white)
#batang7 = cylinder(pos=ball7.pos,axis=ball8.pos-ball7.pos,radius=0.1,color=color.white)
#batang8 = cylinder(pos=ball8.pos,axis=ball9.pos-ball8.pos,radius=0.1,color=color.white)
#batang9 = cylinder(pos=ball9.pos,axis=ball10.pos-ball9.pos,radius=0.1,color=color.white)
#pusat = sphere(pos=vector(4.5,3.25,0), radius=0.2, color=color.red)
#stick = compound([ball, ball2, ball3, ball4, ball5, ball6,
                  #ball7, ball8, ball9, ball10, batang, batang2, batang3, batang4, batang5,
                  #batang6, batang7, batang8, batang9])
#ball.opacity = ball2.opacity = ball3.opacity = ball4.opacity = ball5.opacity
#ball.opacity = ball.opacity
#pusat.velocity = vector(0,0,0)
ball.velocity = vector(0,0,0)
ball10.velocity = vector(0,0,0)
#stick.velocity=vector(0,0,0)
e = 0.2
dt = 0.01
t = 0

tinggi1 = ball.pos.y
tinggi2 = ball10.pos.y
#tinggi3 = pusat.pos.y

jeda = vector(0.5,0.5,0)
while t<100:
    rate (100)
    ball.velocity.y = ball.velocity.y - 9.8*dt -  e*ball.velocity.y*dt
    ball.pos=ball.pos + ball.velocity*dt
    
    
    
    ball10.velocity.y = ball10.velocity.y - 9.8*dt -  e*ball10.velocity.y*dt
    ball10.pos=ball10.pos + ball10.velocity*dt
    
    batang.pos = ball.pos
    batang.axis.y = ball10.pos.y#-batang.pos.y#-batang.pos.y
    #batang.axis.x = batang.length
    
    ball2.pos.y= 0.9*ball.pos.y  #batang.axis  # + jeda
    
    ball3.pos=0.2*ball10.pos
    
    ball4.pos=0.3*ball10.pos
    
    ball5.pos=0.4*ball10.pos
    
    ball6.pos=0.5*ball10.pos
    
    ball7.pos=0.6*ball10.pos
    
    ball8.pos=0.7*ball10.pos
    
    ball9.pos=0.8*ball10.pos
    #pusat.velocity.y = pusat.velocity.y - 9.8*dt -  e*pusat.velocity.y*dt
    #pusat.pos=pusat.pos + pusat.velocity*dt
    
    
    #stick.origin=ball5.pos
    
    t=t+dt
    
    
    if ball.pos.y>tinggi1:
        tinggi1=ball.pos.y
    if ball.pos.y<=ball.radius and ball.velocity.y<0:
        ball.velocity.y = -ball.velocity.y
    if ball10.pos.y>tinggi2:
        tinggi2=ball10.pos.y
    if ball10.pos.y<=ball10.radius and ball10.velocity.y<0:
        ball10.velocity.y = -ball10.velocity.y
    #if pusat.pos.y>tinggi3:
    #    tinggi3=pusat.pos.y
    #if pusat.pos.y<=pusat.radius and pusat.velocity.y<0:
    #    pusat.velocity.y = -pusat.velocity.y
    
    #stick.pos = pusat.pos
    #stick.axis = ball10.pos - ball.pos


