import numpy as np 
import matplotlib.pyplot as plt
class Projectile:
    g=9.81 
    def __init__(self, masa, k):
        self.masa=masa
        self.k=k
    def ubrzanje(self, vx, vy):
        brzina=np.sqrt(vx**2+vy**2)
        ax=-(self.k/self.masa)*brzina*vx
        ay=-self.g-(self.k/self.masa)*brzina*vy
        return ax, ay
    def simuliranje(self, v0, alfa, dt):
        alfa=np.radians(alfa)
        vx=np.cos(alfa)*v0
        vy=np.sin(alfa)*v0
        hor=0
        vert=0   
        horizontalno=[hor]
        vertikalno=[vert]
        while vert >=0:
            ax, ay=self.ubrzanje(vx, vy)
            vx +=ax*dt
            vy +=ay*dt
            hor +=vx*dt
            vert +=vy*dt
            horizontalno.append(hor)
            vertikalno.append(vert)
        return np.array(horizontalno), np.array(vertikalno)

gibanje=Projectile(20, 0.5)
vrijeme=[1, 0.5, 0.25, 0.1, 0.05]
for dt in vrijeme:
    hor,vert=gibanje.simuliranje(35,60,dt)
    plt.plot(hor, vert, label="f*dt")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.title("Simulacija kosog hitca uzimajući u obzir otpor zraka")
    plt.show()
