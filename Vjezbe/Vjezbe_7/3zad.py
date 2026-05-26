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

a = [3, 1, 4, 1, 5, 9, 2, 6] # paran n
b = [3, 1, 4, 1, 5, 9, 2, 6, 5] # neparan n
print(medijan(a))
print(medijan(b))

srednji=medijan(mase)
print("Medijan iznosi", srednji)
print("Medijan pomocu numpya iznosi", np.median(mase))
