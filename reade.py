import numpy
import matplotlib.pyplot
from mpl_toolkits import mplot3d
from tqdm import tqdm

npload = numpy.load("output.npz")
ax = matplotlib.pyplot.axes(projection = "3d")
# progress = tqdm(
#         total=100,
#         desc="渲染",
#         leave=False,
#         unit="b",
#         unit_scale=True
#         )

#npload["location"] [tick][member][x,y,z] -->
#x[member][tick] y[member][tick] z[member][tick]
x, y, z = [], [], []

lenMember = len(npload["location"][0])
ticks = npload["location"]

for member in range(lenMember):
    mx, my, mz = [], [], []
    for tick in ticks: 
        mx.append(tick[member][0])
        my.append(tick[member][1])
        mz.append(tick[member][2])
    x.append(mx)
    y.append(my)
    z.append(mz)
for member in range(lenMember):
    matplotlib.pyplot.plot(x[member],y[member],z[member])
# matplotlib.pyplot.show()
matplotlib.pyplot.savefig("example1.png")
