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
    def simuliranje_euler(self, v0, alfa, dt):
        alfa=np.radians(alfa)
        vx=np.cos(alfa)*v0
        vy=np.sin(alfa)*v0
        hor=0
        vert=0   
        horizontalno=[hor]
        vertikalno=[vert]
        while vert >=0:
            ax,ay=self.ubrzanje(vx, vy)
            vx +=ax*dt
            vy +=ay*dt
            hor +=vx*dt
            vert +=vy*dt
            horizontalno.append(hor)
            vertikalno.append(vert)
        return np.array(horizontalno), np.array(vertikalno)
    def simuliranje_kut(self, v0, alfa, dt):
        alfa=np.radians(alfa)
        vx=v0*np.cos(alfa) 
        vy=v0*np.sin(alfa)
        hor=0
        vert=0
        horizontalno=[hor]
        vertikalno=[vert]
        while vert >=0:
            ax1,ay1=self.ubrzanje(vx, vy)
            vx2=vx+0.5*dt*ax1
            vy2=vy+0.5*dt*ay1
            ax2,ay2=self.ubrzanje(vx2,vy2)
            vx3=vx+0.5*dt*ax2
            vy3=vy+0.5*dt*ay2
            ax3,ay3=self.ubrzanje(vx3,vy3)
            vx4=vx+0.5*dt*ax3
            vy4=vy+0.5*dt*ay3
            ax4,ay4=self.ubrzanje(vx4,vy4)
            hor +=(dt*(vx+2*(vx+0.5*dt*ax1)+2*(vx+0.5*dt*ax2)+(vx+dt*ax3))/6)
            vert +=(dt*(vy+2*(vy+0.5*dt*ay1)+2*(vy+0.5*dt*ay2)+(vy+dt*ay3))/6)
            vx +=dt*(ax1+2*ax2+2*ax3+ax4)/6
            vy +=dt*(ay1+2*ay2+2*ay3+ay4)/6
            horizontalno.append(hor)
            vertikalno.append(vert)
        return np.array(horizontalno), np.array(vertikalno)
gibanje=Projectile(10, 0.1)
dt=0.01
xe, ye=gibanje.simuliranje_euler(30,60,dt)
xk,yk=gibanje.simuliranje_kut(30,60,dt)
plt.plot(xe, ye, label="Eulerova metoda")
plt.plot(xk, yk, label="Runge-Kutta metoda")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Dvije metode za opis gibanja")
plt.grid()
plt.show()


        