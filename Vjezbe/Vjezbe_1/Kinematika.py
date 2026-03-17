#GIBANJE 
#2 zad
import matplotlib.pyplot as plt
import numpy as np
def jednoliko_gibanje():
    F=float(input("Unesi silu u N:"))
    m=float(input("Unesi masu u kg:"))
    a=[F/m]
    dt=0.05 
    t=0
    brzina=[0]
    pomak=[0]
    vrijeme=[0]
    while t < 10:
        akc=F/m
        a.append(akc)

        x=pomak[-1]+ brzina[-1]*dt
        pomak.append(x)
    
        v=brzina[-1]+ akc*dt
        brzina.append(v)

        t +=dt
        vrijeme.append(t)


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
jednoliko_gibanje()
    