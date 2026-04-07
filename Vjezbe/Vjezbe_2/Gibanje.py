import Particle as prt
import math

p1=prt.Particle(10,60, [2,3])
Da=12.2
Dn=p1.range()
print("Razlika u računu je:", round(Dn-Da, 4), "m.")
p1.plot_trajectory()