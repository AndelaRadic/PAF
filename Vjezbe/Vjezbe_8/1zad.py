import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
h0 = 0.54
m = 0.5257
r = 4.025e-3
g = 9.81

h = np.array([0.14,0.17,0.19,0.22,0.25,0.28,0.31,0.34,0.37,0.40])

t = np.array([1.740,1.793,2.043,2.190,2.280,2.417,2.540,2.640,2.670,2.813])

s = h

# (a) log-log fit
x = np.log10(t)
y = np.log10(s)

coef, cov = np.polyfit(x, y, 1, cov=True)

A, B = coef
dA, dB = np.sqrt(np.diag(cov))

print("A =", A, "+/-", dA)
print("B =", B, "+/-", dB)

plt.figure()

plt.scatter(x, y, label='Mjerenja')
plt.plot(x, A*x+B, label='Fit')

plt.xlabel("log(t)")
plt.ylabel("log(s)")
plt.grid()
plt.legend()

plt.show()

# (b) s = a*t^2
x2 = t**2

a = np.sum(x2*s)/np.sum(x2**2)

res = s - a*x2
sigma2 = np.sum(res**2)/(len(s)-1)
da = np.sqrt(sigma2/np.sum(x2**2))

print("a =", a, "+/-", da)

plt.figure()

plt.scatter(x2, s, label='Mjerenja')
plt.plot(x2, a*x2, label='Fit')

plt.xlabel("t² (s²)")
plt.ylabel("s (m)")
plt.grid()
plt.legend()

plt.show()

aef = 2*a
daef = 2*da

Iz = m*r**2*(g/aef - 1)
dIz = m*r**2*g/aef**2 * daef

print("Iz =", Iz, "+/-", dIz)
