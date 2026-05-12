import math 
M=[0.052,0.124,0.168,0.236,0.284,0.336] #Nm
fi=[0.1745,0.3491,0.5236,0.6981,0.8727,1.0472] #rad 
n=len(M)
print("Pojedinačne vrijednosti: \n")
for a in range(n):
    Dt=M[a]/fi[a]
    print(f"Dt{a+1}={Dt}")
zbroj_xy=0
for a in range(n):
    zbroj_xy +=fi[a]*M[a]
zbroj_x2=0
for x in fi:
    zbroj_x2 +=x**2
Dt_reg=zbroj_xy/zbroj_x2
zbroj_y2=0
for y in M:
    zbroj_y2 += y**2
sigma_a=math.sqrt((1/n)*((zbroj_y2/zbroj_x2)-Dt_reg**2))
print("\n Linearna regresija")
print(f"Dt={Dt_reg}")
print(f"sigma_a={sigma_a}")

