#OSNOVE
#4 zadatak

def koordinate():
    li=[]
    for i in range(4):
        i=int(input("Unesi koordinatu:"))
        li.append(i)
    
    k=(li[3] - li[1])/(li[2] - li[0])
    l=li[1]-(k * li[0])
    print("Jednadzba pravca je: y=",k, "x+",l)
koordinate()



