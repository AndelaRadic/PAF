#Formule
import math
tocke=[]
for x in range(10):
    y=float(input(f"Unesi broj {x+1}:"))
    tocke.append(y)
n=len(tocke)
arits=sum(tocke)/n
zbr_kv=0
for y in tocke:
    zbr_kv +=(y-arits)**2
dev=math.sqrt(zbr_kv/(n*(n-1)))
print(f"Aritmeticka sredina iznosi: {arits}")
print(f"Standardna devijacija iznosi: {dev}")

#Gotovi moduli 
import math
import statistics
tocke=[]
for x in range(10):
    y=float(input(f"Unesi broj {x+1}:"))
    tocke.append(y)
sred=statistics.mean(tocke)
d=len(tocke)
suma_kv=sum((y-sred)**2 for y in tocke)
dev=math.sqrt(suma_kv/(d*(d-1)))
print(f"Aritmeticka sredina iznosi: {sred}")
print(f"Standardna devijacija iznosi: {dev}")
