import package.physics as physics
import numpy
import matplotlib
from tqdm import tqdm
from mpl_toolkits import mplot3d

# 参数
a = numpy.array(
        [
            [1.0,1.0,1.0],
            [2.0,2.0,2.0],
            [3.0,3.0,3.0]
            ]
        )
the_location = numpy.array(
    [[-1.1889693067, 0.0, 0,0], [3.8201881837, 0.0, 0.0], [-2.631218877, 0.0, 0.0]]
)
the_v = numpy.array([[0.0, 0.8042120498, 0.0], [0.0, 0.0212794833, 0.0], [0.0, -0.8254915331, 0.0]])
the_m = numpy.array([1.0, 1.0, 1.0])
system = physics.physic(the_location, the_v, the_m)
print(system.location) #不正常
print(the_location) #不正常
print(a) #正常转换数组
x = []
y = []
z = []

time_tick = 10**1
the_total = int(time_tick * system.accuracy**-1)

STEP = 10**4

progress = tqdm(total=the_total, desc="计算轨道", leave=False, unit="tick", unit_scale=True)
for i in range(1, the_total + 1):
    system.tick(system.gravitation_acceleration())

    if i % 10**2 == 0:
        x.append([system.location[i][0] for i in range(system.members)])
        y.append([system.location[i][1] for i in range(system.members)])
        z.append([system.location[i][2] for i in range(system.members)])
    if i % STEP == 0:
        progress.update(STEP)
ax = plt.axes(projection = "3d")
ax.plot3D(x,y,z)
matplotlib.pyplot.savefig("example1.png")
