stuff=[]

def hiking(w,v):
    print(stuff)
    end=True
    for i in stuff:
        if i[0]<=w:
            end=False
    if end:
        return (w,v)

    final=[]
    for i in stuff:
        if i[0]<=w:
            stuff.remove(i)
            final.append(hiking(w-i[0],v+i[1]))
            stuff.append(i)
    return max(final,key=lambda x: x[1])

f=open("hiking.dat")
file=f.readlines()
nfile=int(file[0])
i=0

for o in range(1,nfile+1):
    stuff=[]
    i+=1
    while i<len(file) and file[i]!='\n':
        line=file[i].strip().split()
        stuff.append((int(line[0]),int(line[1])))
        i += 1
    print('Weight Left: %s Total Value: %s' % hiking(20,0))
