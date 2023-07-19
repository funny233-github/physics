import package.physics as physics
import numpy
import random
import copy
from tqdm import tqdm

X = numpy.array([1.0,0.0,0.0])
Y = numpy.array([0.0,1.0,0.0])
Z = numpy.array([0.0,0.0,1.0])

# 参数

the_location = numpy.array([
    -1.1889693067*X,
    3.8201881837*X,
    -2.631218877*X,
    ])
the_v = numpy.array([
    0.8042120498*Y,
    0.0212794833*Y,
    -0.8254915331*Y
    ])
the_m = numpy.array([1.0, 1.0, 1.0])




# the_location = numpy.array([
#     random.uniform(-3.0,3.0)*X+random.uniform(-3.0,3.0)*Y for _ in range(4)
#     ]) 
# the_v = numpy.array([
#     random.uniform(0.0,0.0)*X+random.uniform(0.0,0.0)*Y for _ in range(4)
#     ])
# the_m = numpy.array([
#     random.uniform(1.0,3.0) for _ in range(4)
#     ])
system = physics.physic(the_location, the_v, the_m)



time = 60
totalTick = int(time * system.accuracy**-1)
STEP = 10**3

progress = tqdm(total=totalTick, desc="计算轨道", leave=False, unit="tick", unit_scale=True)

locationResult = []

for i in range(1, totalTick + 1):
    system.tick(system.gravitation_acceleration())

    if i % 10**3 == 0:
        location = copy.deepcopy(system.location)
        locationResult.append(location)
    if i % STEP == 0:
        progress.update(STEP)
numpy.savez("output",location = locationResult)
# locationResult [tick][member][x,y,z] 
