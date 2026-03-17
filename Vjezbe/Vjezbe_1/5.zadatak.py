import matplotlib.pyplot as plt
import numpy as np
def koordinate():
    li=[]
    for i in range(4):
        i=int(input("Unesi koordinatu:"))
        li.append(i)
    
    k=(li[3] - li[1])/(li[2] - li[0])
    l=li[1]-(k * li[0])
    x=np.linspace(li[2]-1,li[0]+1)
    u=input("s za spremanje ili p za prikaz:")
    plt.plot(x,k*x+l)
    plt.xticks()
    plt.title("linearna funkcija")
    plt.xlabel("x")
    plt.ylabel("y")
    if u=="s":
        ime=input("daj naziv datoteke i napiši .pdf:")
        plt.savefig(ime)
    else:
        plt.show()

koordinate()