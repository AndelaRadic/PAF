import numpy as np
import matplotlib.pyplot as plt

np. random . seed (42)
mase_ciste = np. random . normal (loc =2.06 , scale =0.05 , size =57) . tolist ()
mase = mase_ciste + [6.0 , 1.2 , 3.2 , 4.5 , 8.5 , 7.8 , 0.08 , 0.02] # pogreske pri redukciji podataka
def histogram(podaci, k):
    minimum=min(podaci)
    maximum=max(podaci)
    h=(maximum-minimum)/k
    rubne=[minimum+ i*h for i in range(k+1)]
    frekvencije = [0]*k
    for x in podaci:
        for j in range(k):
            if j == k-1:
                if rubne[j] <= x <= rubne[j+1]:
                    frekvencije[j] += 1
                    break
            else:
                if rubne[j] <= x < rubne[j+1]:
                    frekvencije[j] += 1
                    break
    for j in range(k):
        print(f"[{rubne[j]:.3f}, {rubne[j+1]:.3f}) : {frekvencije[j]}")
    return rubne, frekvencije
rubne, frekvencije = histogram(mase_ciste, 10)
sirine = []
for i in range(len(rubne)-1):
    sirine.append(rubne[i+1] - rubne[i])
plt.bar(
    rubne[:-1],
    frekvencije,
    width=sirine,
    align='edge'
)
plt.xlabel("Masa [M☉]")
plt.ylabel("Frekvencija")
plt.title("Histogram masa Sirius A (ručno)")
plt.show()
    