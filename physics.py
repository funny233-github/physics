import matplotlib.pyplot
import numpy


class physic:
    G = 1.0  #引力常量1.0
    accuracy = 10**-5

    def __init__(self, location, v, m):  #m质量,location坐标
        self.location = location
        self.v = v
        self.m = m
        self.members = len(location)

    def tick(self, a):  #a加速度向量,accuracy精度
        self.location += self.v * self.accuracy
        self.v += a * self.accuracy

    def gravitation(self):  #引力函数
        vector = numpy.zeros([self.members, 2])
        for first_object in range(self.members):
            for second_object in range(self.members):
                if second_object == first_object:
                    continue
                second_m = self.m[second_object]
                vector_d = self.location[second_object] - self.location[
                    first_object]
                d = (vector_d[0]**2 + vector_d[1]**2)**0.5
                vector[first_object] += vector_d * second_m / d**3
            first_m = self.m[first_object]
            vector[first_object] *= first_m * self.G
        return vector

    def acceleration(self):  #引力替换成加速度
        acceleration = numpy.zeros([self.members, 2])
        for the_object in range(self.members):
            acceleration[the_object] = self.gravitation(
            )[the_object] / self.m[the_object]
        return acceleration


#三体样例函数
def example():
    #三体参数
    the_location = numpy.array([[-1.1889693067, 0.0], [3.8201881837, 0.0],
                                [-2.631218877, 0.0]])
    the_v = numpy.array([[0.0, 0.8042120498], [0.0, 0.0212794833],
                         [0.0, -0.8254915331]])
    the_m = numpy.array([1.0, 1.0, 1.0])

    system = physic(the_location, the_v, the_m)
    x = []
    y = []

    for i in range(10**6):  #迭代数，也是tick总数
        #system.tick(numpy.array([[0.0,-1.0],[-4.0,+1.0]]))
        system.tick(system.acceleration())
        x.append([system.location[x][0] for x in range(len(system.location))])
        y.append([system.location[x][1] for x in range(len(system.location))])
        if i % 10**4 == 0:  #输出的数字需要符合的等式如1000,2000,3000
            print(i)
    matplotlib.pyplot.plot(x, y)
    matplotlib.pyplot.savefig("nomal.png")


example()
