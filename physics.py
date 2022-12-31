import matplotlib.pyplot
import numpy
class physic:
    G = 1.0#引力常量1.0
    accuracy = 10**-5
    def __init__(self,location,v,m):#m质量,location坐标
        self.location = location
        self.v = v
        self.m = m
    def tick(self,a):#a加速度向量,accuracy精度
        self.location += self.v*self.accuracy
        self.v += a*self.accuracy
def example():
    the_location = numpy.array([[0.0,0.0],[10.0,0.0],[100.0,0.0]])
    the_v = numpy.array([[1.0,0.0],[1.0,0.0],[1.0,0.0]])
    the_m = numpy.array([1.0,1.0,1.0])

    system = physic(the_location,the_v,the_m)
    x = []
    y = []

    for i in range(10**5):
        system.tick(numpy.array([0,-1]))
        x.append([system.location[x][0]for x in range(len(system.location))])
        y.append([system.location[x][1]for x in range(len(system.location))])
        if i % 10**4 == 0:
            print(i)
    matplotlib.pyplot.plot(x,y)
    matplotlib.pyplot.savefig("nomal.png")
example()
