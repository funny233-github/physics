import package.physics as physics
import numpy
import matplotlib
from tqdm import tqdm

# 参数
the_location = numpy.array(
    [[-1.1889693067, 0.0], [3.8201881837, 0.0], [-2.631218877, 0.0]]
)
the_v = numpy.array([[0.0, 0.8042120498], [0.0, 0.0212794833], [0.0, -0.8254915331]])
the_m = numpy.array([1.0, 1.0, 1.0])
system = physics.physic(the_location, the_v, the_m)

x = []
y = []

time_tick = 10**1
the_total = int(time_tick * system.accuracy**-1)

STEP = 10**4

class main(Scene):
    def construct(self):
        the_location = numpy.array(
            [[-1.1889693067, 0.0], [3.8201881837, 0.0], [-2.631218877, 0.0]]
        )
        the_v = numpy.array([[0.0, 0.8042120498], [0.0, 0.0212794833], [0.0, -0.8254915331]])
        the_m = numpy.array([1.0, 1.0, 1.0])
        system = physics.physic(the_location, the_v, the_m)
        
        x = []
        y = []
        
        time_tick = 10**1

        point1 = Dot(color = BLUE)
        point2 = Dot(color = RED)
        point3 = DOT()
        dt = ValueTracker(0)
        def update_path(point):

