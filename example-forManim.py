from manim import *
import numpy
import random


numpyload = numpy.load("output.npz")["location"]
# numpyload [tick][member][x,y,z]

numMenber = len(numpyload[0])
ticks =  len(numpyload)

class main(Scene):
    def construct(self):
        plane = NumberPlane()

        value = ValueTracker(0)

        color = [RED,GREEN,BLUE,YELLOW,WHITE]

        dots  = [Dot(color = random.choice(color)) for _ in range(numMenber)]
        lines = [TracedPath(dot.get_center,dissipating_time=1.0,stroke_opacity=[0,1]) for dot in dots]

        self.add(plane)
        self.add(*dots)
        self.add(*lines)

        def updater(mob):
            # moblocation = [dots.index(mob)][int(value.get_value())]
            tick = int(value.get_value())
            member = dots.index(mob)
            moblocation = numpyload[tick][member]
            mob.move_to(moblocation)
        for dot in dots:
            dot.add_updater(updater)
        self.play(value.animate.set_value(ticks-1),run_time=10,rate_func=linear)
