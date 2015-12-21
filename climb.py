def prnt(c):
    s=0
    m=[]
    line=''
    while c>0:
        line=''
        for i in range(0,s):
            line=line+' '
        for i in range(0, c):
            line=line+'C'
        m.append(line)
        c=c-1
        s=s+1
    return m
f=open('climb.dat')
data=f.readlines()
ndata=int(data[0])

for i in range(1,ndata+1):
    print ' '
    n=data[i]
    final=prnt(int(n))
    for ii in range(len(final),0,-1):
        print final[ii-1]