import Calculus as c
import math
import matplotlib.pyplot as plt
import numpy as np

def fsin(x):
    return math.sin(x)
def sind(x):
    return math.cos(x)

def fcos(x):
    return math.cos(x)
def cosd(x):
    return -math.sin(x)
def fkub(x):
    return x**3
def kubd(x):
    return 3*x**2


print(c.derivacija(fkub, 2, 0.0001)) 
print(c.pravokutna(fkub, 1,4,100))
print(c.trapezna(fkub, 1, 4, 100))

x=np.linspace(-3, 3, 100)
l1=c.tocke(fkub, -3, 3, 0.5)  #iznos derivacija od -2 do 2, h=0.5, c.tocke ce nam dati dvije liste, u jednoj su brojevi, u drugoj su vrijednosti derivacija za njih
l2=c.tocke(fkub, -3, 3, 0.0001)
l3=c.tocke(fkub, -3, 3, 0.01)

plt.title('Derivacija funkcije x^3')
plt.legend()
plt.xlabel('x')
plt.ylabel('df(x)/dx')
plt.plot(x, 3*(x**2))
plt.scatter(l1[0], l1[1], c='purple', s=5)
plt.scatter(l2[0], l2[1], c='orange', s=5)
plt.scatter(l3[0], l3[1], c='blue', s=5)
plt.show()
