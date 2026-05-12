def racun(N):
    a=1/3
    b=5
    for x in range(N):
        b += a
    for x in range(N):
        b -= a
    return b

print("Za 200 iteracija:", racun(200))
print("Za 2000 iteracija:", racun(2000))
print("Za 20000 iteracija:",racun(20000))

    

