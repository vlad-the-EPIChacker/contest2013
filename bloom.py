f=open("bloom.in")
file=f.readlines()
nfile=int(file[0])
c=0
l=1

while c<nfile:
    ltf=int(file[l])
    bloom=0
    flos=[file[i].split() for i in range(l+1, ltf+l+1)]
    day=int(file[l+ltf+1])
    for i in range(0, len(flos)):
        flo=flos[i]
        flo=[int(ii) for ii in flo]
        s=flo[len(flo)-1]
        flo=flo[0:len(flo)-1]
        if s<0:
            sum2=0
        else:
            sum2 = sum(flo[s:])
        sum1=sum(flo)
        if sum2>0:
            n=float(day-sum1)
            n=n/sum2
            if n==int(n):
                bloom += 1
        elif sum1==day:
            bloom += 1
    print bloom
    c += 1
    l += ltf +2
