from manim import *
import numpy
import random
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
        value = ValueTracker(0)
        color = [RED,GREEN,BLUE,YELLOW,WHITE]
        dots = [Dot(color = random.choice(color)) for _ in range(len(location))]
        lines = [TracedPath(dot.get_center,dissipating_time=1.0,stroke_opacity=[0,1]) for dot in dots]
        self.add(*dots)
        self.add(*lines)
        def updater(mob):
            mob.move_to(location[dots.index(mob)][int(value.get_value())])
        for dot in dots:
            dot.add_updater(updater)
        self.play(value.animate.set_value(len(locationRead["x"])-1),run_time=10,rate_func=linear)
