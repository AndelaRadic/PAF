import numpy as np
import matplotlib.pyplot as plt

q= 1.60e-19
qe= -1.60e-19
m = 9.11e-31
B = np.array([0, 0,5e-3])   
#Pocetni uvjeti
r=np.array([0.0, 0.0, 0.0])
v=np.array([2e5, 4e5, 4e4])
dt = 1e-12
raz=20000
def akc(dq,dv,E):
    F = E + np.cross(dv, B)
    return (dq/m) * F

def r_kut(dq, dr, dv, dt, E):
    k1v = akc(dq, dv, E)
    k1r = dv

    k2v = akc(dq, dv + 0.5*dt*k1v, E)
    k2r = dv + 0.5*dt*k1v

    k3v = akc(dq, dv + 0.5*dt*k2v, E)
    k3r = dv + 0.5*dt*k2v

    k4v = akc(dq, dv + dt*k3v, E)
    k4r = dv + dt*k3v

    brzina = dv + (dt/6)*(k1v + 2*k2v + 2*k3v + k4v)
    pomak = dr + (dt/6)*(k1r + 2*k2r + 2*k3r + k4r)

    return brzina, pomak

def simulacija(dq, E):
    dr = []
    dv = []

    dr.append(r.copy())
    dv.append(v.copy())

    for i in range(raz - 1):
        brzina, pomak = r_kut(dq, dr[i], dv[i], dt, E)
        dr.append(pomak)
        dv.append(brzina)

    return np.array(dr)

slika = plt.figure()
ax = slika.add_subplot(projection = "3d")

pts = simulacija(qe, np.array([0,0,0]))
x = []
y = []
z = []
for t in pts:
    x.append(t[0])
    y.append(t[1])
    z.append(t[2])
ax.plot(x, y, z, label = "E = 0", linewidth = 2)

pts = simulacija(qe, np.array([0,0,100]))
x = []
y = []
z = []
for s in pts:
    x.append(s[0])
    y.append(s[1])
    z.append(s[2])
ax.plot(x, y, z, label = "E || B", linewidth = 2)

pts = simulacija(qe, np.array([100,0,0]))
x = []
y = []
z = []
for p in pts:
    x.append(p[0])
    y.append(p[1])
    z.append(p[2])
ax.plot(x, y, z, label = "E ⊥ B", linewidth = 2)

ax.legend()
ax.set_xlabel("x", labelpad=15, fontsize=13)
ax.set_ylabel("y", labelpad=15, fontsize=13)
ax.set_zlabel("z", labelpad=15, fontsize=13)
plt.title("Elektron")
ax.set_box_aspect([1,1,1])
plt.show()
fig = plt.figure()
ax = fig.add_subplot(projection = "3d")

pts = simulacija(q, np.array([0,0,0]))
x = []
y = []
z = []
for t in pts:
    x.append(t[0])
    y.append(t[1])
    z.append(t[2])
ax.plot(x, y, z, label = "E = 0", linewidth = 1)

pts = simulacija(q, np.array([0,0,100]))
x = []
y = []
z = []
for p in pts:
    x.append(p[0])
    y.append(p[1])
    z.append(p[2])
ax.plot(x, y, z, label = "E || B", linewidth = 1)

pts = simulacija(q, np.array([100,0,0]))
x = []
y = []
z = []
for s in pts:
    x.append(s[0])
    y.append(s[1])
    z.append(s[2])
ax.plot(x, y, z, label = "E ⊥ B", linewidth = 1)

ax.legend()
ax.set_xlabel("x", labelpad=15, fontsize=13)
ax.set_ylabel("y", labelpad=15, fontsize=13)
ax.set_zlabel("z", labelpad=15, fontsize=13)
plt.title("Pozitron")
ax.set_box_aspect([1,1,1])
plt.show()
    
















