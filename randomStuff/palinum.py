f=open("palinum.dat")
file=f.readlines()
nfile=int(file[0])

for i in range(1, nfile+1):
    n=int(file[i])
    for ii in range(0,5):
        reversed=int(str(n)[::-1])
        if n==reversed:
            break
        n+=reversed
    print n