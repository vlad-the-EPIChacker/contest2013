f=open("survey.dat")
file=f.readlines()
nfile=int(file[0])

for i in range(1, nfile+1):
    m=int(file[i].strip().split()[0])
    n=int(file[i].strip().split()[1])
    sur=['' for ii in range(0, m+1)]
    for ii in range(1,n+1):
        ch=chr(ord('A')+ii-1)
        for iii in range(ii,len(sur),ii):
            sur[iii]+=ch
    big=[]
    bign=0
    for ii in sur:
        if len(ii)>bign:
            bign = len(ii)
    for ii in sur:
        if len(ii)==bign:
            big.append(str(sur.index(ii)))
    print "Box that contained the most surveys:",' '.join(big)
    print "Box",n,"contains",len(sur[n]),"surveys."
    only=[]
    for ii in range(0,len(sur)):
        if sur[ii] == 'A':
            only.append(str(ii))
    print "Boxes that contained only survey A:",' '.join(only)
    thre=[]
    for ii in sur:
        if len(ii)==3:
            thre.append(str(sur.index(ii)))
    print "Boxes that contained exactly three surveys:",' '.join(thre)
    sur=[len(ii) for ii in sur]
    print "Total number of surveys stuffed:",sum(sur)
    print ""
