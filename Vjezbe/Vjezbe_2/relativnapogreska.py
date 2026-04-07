import math
import matplotlib.pyplot as plt
import numpy as np
v0=10
ß=60
def graf(v0, ß):
    def pogreska(v0, ß, dt):
        def analitickiD(v0, ß):
            D=((v0**2)*math.sin(2*math.radians(ß)))/9.81
            return D

        def numerickiD(v0, ß, dt):
            vx=v0*math.cos(math.radians(ß))
            vy=v0*math.sin(math.radians(ß))
            x=0
            y=0
            xl=[x]
            yl=[y]
            while y>0:
                x+=vx*dt
                y+=vy*dt
                vy=vy-9.81*dt
            return x
        p=(math.fabs(numerickiD(v0, ß, dt)-analitickiD(v0, ß))/(analitickiD(v0, ß)))*100
        return p 

    t= [i * 0.001 for i in range(1, 105)]
    pogreske=[]
    for i in t:
        p=pogreska(v0, ß, i)
        pogreske.append(p)
   
    plt.xlabel('dt')
    plt.ylabel('pogreška u %')
    plt.plot(t, pogreske)
    plt.show()
graf(v0, ß)
        
    



        