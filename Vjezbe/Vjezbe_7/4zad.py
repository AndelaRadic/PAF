import matplotlib.pyplot as plt 
import numpy as np 
np. random . seed (42)
mase_ciste = np. random . normal (loc =2.06 , scale =0.05 , size =57) . tolist ()
mase = mase_ciste + [6.0 , 1.2 , 3.2 , 4.5 , 8.5 , 7.8 , 0.08 , 0.02] # pogreske pri redukciji podataka
def medijan(podaci):
    sortirano=sorted(podaci)
    n=len(sortirano)
    if n%2==1:
        return sortirano[n//2]
    else:
        return (sortirano[n//2 -1]+ sortirano[n//2]) /2
sredina1 = np.mean(mase)
medijan1 = medijan(mase)

print("Sredina =", sredina1)
print("Medijan =", medijan1)

print("Razlika =", abs(sredina1 - medijan1))

mase_bez = []
for x in mase:
    if 1.5 <= x <= 2.5:
        mase_bez.append(x)

sredina2 = np.mean(mase_bez)
medijan2 = medijan(mase_bez)

print("Nova sredina =", sredina2)
print("Novi medijan =", medijan2)
print(
    "Promjena sredine =",
    abs(sredina2 - sredina1)
)
print(
    "Promjena medijana =",
    abs(medijan2 - medijan1)
)
plt.hist(
    mase,
    bins=10,
    edgecolor='black'
)
plt.axvline(
    sredina1,
    color='red',
    label='Sredina (sve)'
)
plt.axvline(
    medijan1,
    color='blue',
    label='Medijan (sve)'
)
plt.axvline(
    sredina2,
    color='green',
    linestyle='--',
    label='Sredina (bez iznimnih vrijednosti)'
)
plt.axvline(
    medijan2,
    color='magenta',
    linestyle='--',
    label='Medijan (bez iznimnih vrijednosti)'
)
plt.xlabel("Masa [M]")
plt.ylabel("Frekvencija")
plt.title("Utjecaj grubih pogrešaka")
plt.legend()

plt.show()