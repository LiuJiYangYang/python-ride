def triangles():
    tri=[1]
    while 1:
        yield tri
        t=[tri[0]+2]
        tri=t+[tri[i]+tri[i+1] for i in range(len(tri)-1)]+t

n=0
results=[]
for t in triangles():
    print(t)
    results.append(t)
    n=n+1
    if n==10:
        break