import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
kut_deg = np.array([0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85])

theta = np.deg2rad(kut_deg)

T120 = np.array([0.8020,0.8187,0.8327,0.8660,0.8980,0.9153,0.9293,0.9653,0.9747,1.0200,1.0373,1.1160,
                 1.1780,1.2733,1.4180,1.6373,1.9100,2.5460])

T240 = np.array([1.0140,1.0320,1.0433,1.0673,1.0840,1.1320,1.1440,1.1720,1.1980,1.2293,1.2813,1.3573,
                 1.4200,1.5600,1.7413,1.9840,2.4473,3.1573])

g = 9.81

# model za fit
def period(theta, l):
    return 2*np.pi*np.sqrt(l/(g*np.cos(theta)))

# ----- L = 120 mm -----

popt120, pcov120 = curve_fit(period, theta, T120,p0=[0.12], bounds=(0, np.inf))

l120 = popt120[0]
dl120 = np.sqrt(pcov120[0,0])

rel120 = abs(l120 - 0.120)/0.120*100

print("L = 120 mm")
print(f"l = {l120:.5f} ± {dl120:.5f} m")
print(f"Relativna pogreška = {rel120:.2f} %")

# ----- L = 240 mm -----

popt240, pcov240 = curve_fit(period, theta, T240,p0=[0.24], bounds=(0, np.inf))

l240 = popt240[0]
dl240 = np.sqrt(pcov240[0,0])

rel240 = abs(l240 - 0.240)/0.240*100

print("\nL = 240 mm")
print(f"l = {l240:.5f} ± {dl240:.5f} m")
print(f"Relativna pogreška = {rel240:.2f} %")

# ----- graf -----

theta_fine = np.linspace(0, np.deg2rad(85), 500)
kut_fine = np.rad2deg(theta_fine)

plt.figure(figsize=(10,6))

# mjerenja
plt.scatter(kut_deg, T120, label='Mjerenja 120 mm')
plt.scatter(kut_deg, T240, label='Mjerenja 240 mm')

# fit
plt.plot(kut_fine,
         period(theta_fine, l120),
         label=f'Fit 120 mm (l={l120:.3f} m)')

plt.plot(kut_fine,
         period(theta_fine, l240),
         label=f'Fit 240 mm (l={l240:.3f} m)')

# teorija
plt.plot(kut_fine,
         period(theta_fine, 0.120),
         '--',
         label='Teorija 120 mm')

plt.plot(kut_fine,
         period(theta_fine, 0.240),
         '--',
         label='Teorija 240 mm')

plt.xlabel("Kut θ (°)")
plt.ylabel("Period T (s)")
plt.title("Fizikalno njihalo")
plt.grid(True)
plt.legend()
plt.show()

