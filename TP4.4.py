
from turtle import *

###################################

def triangle(c):
    for cote in range(0,3):
        forward(c)
        left(120)


def triangleBas(c):
    for cote in range(0,3):
        forward(c)
        right(120)


def carre(c):
    for cote in range(0,4):
        forward(c)
        right(90)


def polygone(c,n):
    for cote in range(0,n):
        forward(c)
        right(360/n)


def rayons(c,n):
    for cote in range(0,n):
        forward(c)
        back(c)
        right(360/n)

def lignedeCarres(c,n):
    for i in range(0,n):
        carre(c)
        up()
        forward(2*c)
        down()
            
        
    
        
        

#########################################
##triangle(120)
##
##triangleBas(150)
##carre(150)
##polygone(150,5)
##rayons(100,6)
lignedeCarres(50,3)

