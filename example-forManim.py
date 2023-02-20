from manim import *
import numpy
locationRead = numpy.load("output.npz")
location = []
for member in range(len(locationRead["x"][0])):
    members = []
    for i in range(len(locationRead["x"])):
        members.append([
            float(locationRead["x"][i][member]),
            float(locationRead["y"][i][member]),
            float(locationRead["z"][i][member])
            ])
        print(len(members))
    location.append(members)
print(len(location[0]))

class main(Scene):
    def construct(self):
        plane = NumberPlane()
        self.add(plane)
        d1,d2,d3 = Dot(color=RED),Dot(color=GREEN),Dot(color=BLUE)
        line1 = TracedPath(d1.get_center,dissipating_time=0.5,stroke_opacity=[0,1])
        line2 = TracedPath(d2.get_center,dissipating_time=0.5,stroke_opacity=[0,1])
        line3 = TracedPath(d3.get_center,dissipating_time=0.5,stroke_opacity=[0,1])
        value = ValueTracker(0)
        d1.add_updater(lambda z : z.move_to(
            location[0][int(value.get_value())]
            ))
        d2.add_updater(lambda z : z.move_to(
            location[1][int(value.get_value())]
            ))
        d3.add_updater(lambda z : z.move_to(
            location[2][int(value.get_value())]
            ))
        # for i in range(len(location)):
            # dot = Dot(color=GREEN)
            # dot.add_updater(lambda z:z.move_to(
                # location[i][int(value.get_value())]
                # ))
        #     self.add(dot)
        self.add(d1,d2,d3,line1,line2,line3)
        self.play(value.animate.set_value(len(locationRead["x"])-1),run_time=10,rate_func=linear)
