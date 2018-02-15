def fam(cur,dest):
    if cur==dest:
        return True
    for i in relate[cur]:
        relate[cur].remove(i)
        f=fam(i,dest)
        relate[cur].append(i)
        if f:
            return True
    return False

f=open('family.dat')
file=f.readlines()
nfile1=int(file[0])
nfile2=int(file[nfile1+1])
stuff1=[[i.split()[0],i.split()[2]] for i in file[1:nfile1+1]]
stuff2=[i.split() for i in file[nfile1+2:nfile1+nfile2+2]]
relate={}

for i in stuff1:
    if i[0] not in relate.keys():
        relate[i[0]]=[]
    if i[1] not in relate.keys():
        relate[i[1]]=[]
    relate[i[0]].append(i[1])
    relate[i[1]].append(i[0])

for i in stuff2:
    if i[0] in relate.keys():
        if fam(i[0],i[1]):
            print('Related')
        else:
            print('Not Related')
    else:
        print('Not Related')