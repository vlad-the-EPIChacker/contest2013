f=open('similar.dat')
sides=f.readlines()
ndata=int(sides[0])

for i in range(1,ndata+1):
    ns=sides[i].rstrip('\r\n')
    ns=ns.split()
    nI=int(ns[0])
    nIII=int(ns[2])
    nIV=int(ns[3])
    f=float(nIV)/nI
    prnt=f*nIII
    print nIV, ns[4], int(prnt)