import numpy
import matplotlib.pyplot
from mpl_toolkits import mplot3d
from tqdm import tqdm

location = numpy.load("output.npz")
ax = matplotlib.pyplot.axes(projection = "3d")
progress = tqdm(
        total=len(location["x"][0]),
        desc="渲染",
        leave=False,
        unit="b",
        unit_scale=True
        )
for members in range(len(location["x"][0])):
    xx = [location["x"][i][members] for i in range(len(location["x"]))]
    yy = [location["y"][i][members] for i in range(len(location["y"]))]
    zz = [location["z"][i][members] for i in range(len(location["z"]))]
    ax.plot3D(xx,yy,zz)
    progress.update(1)
# matplotlib.pyplot.show()
matplotlib.pyplot.savefig("example1.png")
