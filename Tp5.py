from turtle import *

##
def spirale(r):

    a = 1
    b = 50
    x = 450
    color("red")
    speed("normal")
 
    
    for cote in range(x):
    
       forward(b)
       left(a)
       a = a + 5
       

def spirale(r):
    rayon=20
    speed(20)
    while rayon<r:
        circle(rayon,180)
        rayon+=10
        pensize(5)
        color ("red")
        circle(30,280)
        rayon+=5
        color("green")
    

spirale (350)
from math import pi, sin, cos
def spirale2(h):
    rayon = 20
    speed(100)
    
    n=50 #number of spirals
    d=10 #distance between 2 spirals
    r=0  #radius
    x,y = 0, 0

    cur_r = r
    for i in range(n):
        for a in range(1,360, 4):
            r = cur_r + d*a/360.0
            a *= pi/180.0
            y = r*sin(a)
            x = r*cos(a)
            goto(x,y)
        cur_r += d
spirale2(350)      
