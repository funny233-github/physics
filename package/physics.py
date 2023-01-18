import numpy


class physic:
    G = 1.0  # 引力常量1.0
    accuracy = 10**-4  # 精度

    def __init__(self, location, v, m):  # m质量,location坐标,v速度向量,members对象数量
        self.location = location
        self.v = v
        self.m = m
        self.members = len(location)

    def tick(self, a):  # a加速度向量,accuracy精度
        self.location += self.v * self.accuracy
        self.v += a * self.accuracy

    def gravitation_acceleration(self):  # 引力加速度函数
        vector = numpy.zeros([self.members, 3])
        for first_object in range(self.members):
            for second_object in range(first_object + 1, self.members):
                second_m = self.m[second_object]
                vector_d = self.location[second_object] - self.location[first_object]
                d = self.modulus(vector_d)
                first_m = self.m[first_object]
                vector[first_object] += vector_d * second_m / d**3
                vector[second_object] += -vector[first_object] * first_m / second_m
        return vector * self.G

    def acceleration(self, vector_force):  # (alpha)力替换成加速度
        acceleration = numpy.zeros([self.members, 3])
        for the_object in range(self.members):
            acceleration[the_object] = vector_force()[the_object] / self.m[the_object]
        return acceleration

    def dynatic_energy(self):  # 动能计算
        energy = numpy.zeros([self.members])
        for the_object in range(self.members):
            v = self.modulus(self.v[the_object])
            energy[the_object] += 0.5 * self.m[the_object] * v**2
        return energy

    def momentum(self):  # 动量计算
        vector_momentum = numpy.zeros([self.members, 3])
        for the_object in range(self.members):
            vector_momentum[the_object] += self.v[the_object] * self.m[the_object]
        return vector_momentum

    def modulus(self, vector):  # 向量模计算,vecotr指仅仅含有xy的向量
        return (vector[0] ** 2 + vector[1] ** 2 + vector[2] ** 2) ** 0.5

    def center_m(self):  # 质点计算
        vector_center = numpy.zeros(3)
        M = 0
        for i in range(self.members):
            vector_center += self.m[i] * self.location[i]
            M += self.m[i]
        return vector_center / M
