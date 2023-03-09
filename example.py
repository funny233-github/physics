import package.physics as physics
import numpy
import matplotlib.pyplot
import random
from tqdm import tqdm
from mpl_toolkits import mplot3d

X = numpy.array([1.0,0.0,0.0])
Y = numpy.array([0.0,1.0,0.0])
Z = numpy.array([0.0,0.0,1.0])

# 参数
# the_location = numpy.array([
    # -1.1889693067*X,
    # 3.8201881837*X,
    # -2.631218877*X,
#     ])
the_location = numpy.array([
    random.uniform(1.0,3.0)*X+random.uniform(1.0,3.0)*Y for _ in range(4)
    ])
# the_v = numpy.array([
    # 0.8042120498*Y,
    # 0.0212794833*Y,
    # -0.8254915331*Y
#     ])
the_v = numpy.array([
    random.uniform(1.0,3.0)*X+random.uniform(1.0,3.0)*Y for _ in range(4)
    ])
# the_m = numpy.array([1.0, 1.0, 1.0])
the_m = numpy.array([
    random.uniform(1.0,3.0) for _ in range(4)
    ])
system = physics.physic(the_location, the_v, the_m)
x = []
y = []
z = []

time_tick = 60
the_total = int(time_tick * system.accuracy**-1)

STEP = 10**3

progress = tqdm(total=the_total, desc="计算轨道", leave=False, unit="tick", unit_scale=True)
for i in range(1, the_total + 1):
    system.tick(system.gravitation_acceleration())

    if i % 10**3 == 0:
        x.append([system.location[i][0] for i in range(system.members)])
        y.append([system.location[i][1] for i in range(system.members)])
        z.append([system.location[i][2] for i in range(system.members)])
    if i % STEP == 0:
        progress.update(STEP)
numpy.savez("output",x = x,y = y,z = z)
# ax = matplotlib.pyplot.axes(projection = "3d")
# for members in range(system.members):
    # xx = [x[i][members] for i in range(len(x))]
    # yy = [y[i][members] for i in range(len(y))]
    # zz = [z[i][members] for i in range(len(z))]
    # ax.plot3D(xx,yy,zz)
# matplotlib.pyplot.show()
# matplotlib.pyplot.savefig("example1.png")
