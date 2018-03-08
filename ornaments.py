def L(x):
    t1=1
    for i in range(2,x+1):
        t1 += t1 + i +1
    return t1

f=open("ornaments.dat")
file=f.readlines()
nfile=int(file[0])

for i in range(1,nfile+1):
    n=int(file[i])
    t=1
    t1=1
    for x in range(2,n+1):
        t1 = t1 + x
        t+=t1
    print(t)