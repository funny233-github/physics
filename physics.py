import matplotlib.pyplot
import numpy
class physic:
    G = 1.0#引力常量1.0
    def __init__(self,x,y,vx,vy,m):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.m = m
