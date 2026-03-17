#OSNOVE
#3 zadatak
while True:
    x1=input("Unesi broj:")
    if x1.isdigit():          
        x1=int(x1)
        print(x1)
        break
    else:
        print("Ponovno unesi")
while True:
    y1=input("Unesi broj:")
    if y1.isdigit():        
        y1=int(y1)
        print(y1)
        break
    else:
        print("Ponovno unesi")
while True:
    x2=input("Unesi broj:")
    if x2.isdigit():       
        x2=int(x2)
        print(x2)
        break
    else:
        print("Ponovno unesi")
while True:
    y2=input("Unesi broj:")
    if y2.isdigit():     
        y2=int(y2)
        print(y2)
        break
    else:
        print("Ponovno unesi")
if x1==x2:
    print("jedanadzba pravca je x=:",x1)
else:
    k=(y2-y1)/(x2-x1)
    l=y1-(k*x1)
    print("Jednadzba pravca je y=:",k, "x+", l)

