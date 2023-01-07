import matplotlib.pyplot
import numpy
from tqdm import tqdm


class physic:
    G = 1.0  # 引力常量1.0
    accuracy = 10**-4

    def __init__(self, location, v, m):  # m质量,location坐标
        self.location = location
        self.v = v
        self.m = m
        self.members = len(location)  # 获取总共有都少要计算的物体数

    def tick(self, a):  # a加速度向量,accuracy精度
        self.location += self.v * self.accuracy
        self.v +=a * self.accuracy

    def gravitation_acceleration(self):  # 引力加速度函数
        vector = numpy.zeros([self.members, 2])
        for first_object in range(self.members):
            for second_object in range(first_object+1,self.members):
                second_m = self.m[second_object]
                vector_d = self.location[second_object] - self.location[first_object]
                d = self.modulus(vector_d)
                first_m = self.m[first_object]
                vector[first_object] += vector_d * second_m / d**3
                vector[second_object] += -vector[first_object] * first_m / second_m
        return vector*self.G

#    def acceleration(self):  # 引力替换成加速度
#        acceleration = numpy.zeros([self.members, 2])
#        for the_object in range(self.members):
#            acceleration[the_object] = (
#                self.gravitation()[the_object] / self.m[the_object]
#            )
#        return acceleration

    def dynatic_energy(self):  # 动能计算
        energy = numpy.zeros([self.members])
        for the_object in range(self.members):
            v = self.modulus(self.v[the_object])
            energy[the_object] += 0.5 * self.m[the_object] * v**2
        return energy

    def modulus(self, vector):  # 向量模计算,vecotr指仅仅含有xy的向量
        return (vector[0] ** 2 + vector[1] ** 2) ** 0.5


# 三体样例函数
def example1():
    # 三体参数
    the_location = numpy.array(
        [[-1.1889693067, 0.0], [3.8201881837, 0.0], [-2.631218877, 0.0]]
    )
    the_v = numpy.array(
        [[0.0, 0.8042120498], [0.0, 0.0212794833], [0.0, -0.8254915331]]
    )
    the_m = numpy.array([1.0, 1.0, 1.0])

    # 初始化三体系统
    system = physic(the_location, the_v, the_m)

    # 记录用的列表
    x = []
    y = []
    #energy = []
    #total_energy = []
    #time = []

    # 总tick数
    the_total = 10**5
    # 进度条更新间隔
    STEP = 10**4

    # 进度条对象，必须在同一个对象上更新才有效果
    progress = tqdm(
        total=the_total, desc="计算轨道", leave=False, unit="tick", unit_scale=True
    )

    for i in range(1, the_total + 1):  # 迭代数，也是tick总数
        system.tick(system.gravitation_acceleration())

        if i % 10**2 == 0:  # 设置采样方式，减少内存占用
            x.append([system.location[x][0] for x in range(system.members)])
            y.append([system.location[x][1] for x in range(system.members)])
            #energy.append([system.dynatic_energy()[x] for x in range(system.members)])
            #total_energy.append(numpy.sum(system.dynatic_energy()))
            #time.append(i * system.accuracy)

        if i % STEP == 0:
            # .update() 方法的参数值是进度条的更新增量
            progress.update(STEP)

    progress.close()  # 关闭进度条
    matplotlib.pyplot.plot(x,y)
    # matplotlib.pyplot.plot(time, energy)
    # matplotlib.pyplot.plot(time, total_energy)
    matplotlib.pyplot.savefig("example1.png")
  
def example2():
    member = 10
    the_location = numpy.random.randn(member, 2)
    the_v = numpy.random.randn(member, 2)
    the_m = numpy.random.randn(member)

    system = physic(the_location, the_v, the_m)

    x = []
    y = []

    the_total = 10**5
    STEP = 10**4

    progress = tqdm(
        total=the_total, desc="计算轨道", leave=False, unit="tick", unit_scale=True
    )
    for i in range(1, the_total + 1):        
        system.tick(system.gravitation_acceleration())
        if i % 10**2 == 0:
            x.append([system.location[x][0] for x in range(system.members)])
            y.append([system.location[x][1] for x in range(system.members)])
        if i % STEP == 0:
            progress.update(STEP)
    progress.close()
    matplotlib.pyplot.plot(x, y)
    matplotlib.pyplot.savefig("example2.png")

example2()
