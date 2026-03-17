#GIBANJE
#1 zadatak
import matplotlib.pyplot as plt
import numpy as np

F=float(input("Unesi silu u N:"))
m=float(input("Unesi masu u kg:"))
a=[F/m]
dt=0.05 
t=0
brzina=[0]
pomak=[0]
vrijeme=[0]
while t < 10:
    t +=dt
    vrijeme.append(t)

    akc=F/m
    a.append(akc)
    
    v=brzina[-1]+ akc*dt
    brzina.append(v)
    
    x=pomak[-1]+ brzina[-1]*dt+ 0.5*akc*dt**2
    pomak.append(x)

plt.plot(vrijeme,a)
plt.title("a-t graf")
plt.xlabel("t/s")
plt.ylabel("a_m/s**2")
plt.show()
plt.plot(vrijeme,brzina)
plt.title("v-t graf")
plt.xlabel("t/s")
plt.ylabel("v_m/s")
plt.show()
plt.plot(vrijeme,pomak)
plt.title("x-t graf")
plt.xlabel("t/s")
plt.ylabel("x/m")
plt.show()






