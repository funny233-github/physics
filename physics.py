import matplotlib.pyplot
import numpy
class physic:
#############
#   define  #
#############
    G = 1.0#引力常量1.0
    accuracy = 10**-10
#############
#   init    #
#############
    def __init__(self,location,v,m):#m质量,location坐标
        self.location = location
        self.v = v
        self.m = m

    def tick(self,a):#a加速度向量,accuracy精度
        self.location += self.location*self.accuracy
        self.v += a*self.accuracy
def example():
    the_location = numpy.array([[0.0,0.0],[10.0,0.0],[100.0,0.0]])
    the_v = numpy.array([[0.0,0.0],[0.0,0.0],[0.0,0.0]])
    the_m = numpy.array([1.0,1.0,1.0])

    way = numpy.array([])
    way = numpy.append(way,the_location)

    system = physic(the_location,the_v,the_m)

    for i in range(10):
        system.tick(numpy.array([0,-1]))
        way = numpy.append(way,system.location)
example()
