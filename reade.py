import numpy
import matplotlib.pyplot
from mpl_toolkits import mplot3d

location = numpy.load("output.npz")
ax = matplotlib.pyplot.axes(projection = "3d")
for members in range(len(location["x"][0])):
    xx = [location["x"][i][members] for i in range(len(location["x"]))]
    yy = [location["y"][i][members] for i in range(len(location["y"]))]
    zz = [location["z"][i][members] for i in range(len(location["z"]))]
    ax.plot3D(xx,yy,zz)
matplotlib.pyplot.show()
matplotlib.pyplot.savefig("example1.png")
