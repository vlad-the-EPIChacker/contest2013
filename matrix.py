def det(col,row):
    sum=0
    if len(col)==2:
        #print "2x2",m[row[0]][col[0]], m[row[1]][col[1]],m[row[0]][col[1]],m[row[1]][col[0]]
        return m[row[0]][col[0]]*m[row[1]][col[1]]-m[row[0]][col[1]]*m[row[1]][col[0]]
    x=0
    for y in range(0,len(col)):
        row1=[row[ii] for ii in range(0, len(row)) if ii!=x]
        col1=[row[ii] for ii in range(0, len(col)) if ii!=y]
        sum1=det(col1,row1)
        co=m[row[x]][col[y]]
        if y%2==1:
            co *= -1
        if len(col)==4:
            print "3x3",sum1,co
        if len(col)==3:
            print sum1,co
        sum1 *= co
        sum += sum1
    return sum



f=open("matrix.dat")
file=f.readlines()
ncases=int(file[0])
l=1
c=0

while c<ncases:
    nlines=len(list(file[l].strip()))
    m=[list(file[l+i].strip()) for i in range(0, nlines)]
    m=[[int(ii) for ii in i]for i in m]
    print det([i for i in range(0,len(m))],[i for i in range(0,len(m))])
    l += nlines
    c+=1
    print 'c =',c
