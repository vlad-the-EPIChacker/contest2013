def fib(n):
    x=0
    y=1
    for i in range(0,n):
        x += y
        y += x
    return y

f=open("bunny.dat")
file=f.readlines()
nfile=int(file[0])

for i in range(1,nfile+1):
    print(fib(int(file[i])))