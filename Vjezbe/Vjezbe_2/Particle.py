import math
import matplotlib.pyplot as plt
import numpy as np
class Particle:
    def __init__(self, v0, ß, xy):
        self.v0=v0
        self.ß=math.radians(ß)
        self.xy=xy 
        self.x=xy[0]
        self.y=xy[1]
        self.xl=[self.x]
        self.yl=[self.y]
        self.vx=v0*math.cos(self.ß)
        self.vy=v0*math.sin(self.ß)
    
    def reset(self):
        self.xy=0
        self.ß=0
        self.v0=0
    
    def __move(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.g=9.81
        self.vy -= self.g * dt
        self.xl.append(self.x)
        self.yl.append(self.y)

    def range(self):
        dt=0.03
        while self.y >= 0:      
            self.__move(dt)
        return self.x
    
    def plot_trajectory(self):
        import matplotlib.pyplot as plt
        plt.xlabel('x/m')
        plt.ylabel('y/m')
        plt.title('Gibanje čestice')
        plt.plot(self.xl, self.yl)
        return plt.show()
        



