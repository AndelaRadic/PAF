def derivacija(f, x0, y0, m='three-step'):
    if m=='three-step':
        return round((f(x0+y0) - f(x0-y0))/(2*y0), 4)
    elif m=='two-step':
        return round((f(x0+y0)-f(x0))/(y0), 4)
    else:
        raise ValueError ('Metoda mora biti three-step ili two-step')

def tocke(f, a, b, y):
    import numpy as np
    br=np.arange(a, b +0.1, 0.1)
    br=br.tolist()
    der=[]
    for j in br:
        d=(f(j+y)-f(j-y))/(2*y)
        der.append(round(d, 4))

    return [br, der]

def pravokutna(f, a, b, n):
    dx=(b-a)/n
    g=0     
    d=0
    for i in range(n):
        d+= f(a+i*dx)*dx
        g+= f(a+(i+1)*dx)*dx
    return [round(g, 4), round(d, 4)]
    
def trapezna(f, a, b, n):
    dx=(b-a)/n
    s=0
    for i in range (n):
        s+=f(a+dx*i)+f(a+dx*(i+1))
    return round(s*dx/2, 4)