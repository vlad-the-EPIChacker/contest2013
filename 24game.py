def DFS(ns,s):
    #print(s)
    if s==24 and len(ns)==0:
        #print(ns,len(ns))
        return True
    for n in ns:
        tempNs=[i for i in ns]
        tempNs.remove(n)
        if DFS(tempNs,s+n):
            #print(s,'+',n,'=',s+n)
            return True
        if s>0:
            if DFS(tempNs,s-n):
                #print(s, '-', n, '=', s - n)
                return True
            if DFS(tempNs,s*n):
                #print(s, '*', n, '=', s * n)
                return True
            if DFS(tempNs,s/n):
                #print(s, '/', n, '=', s / n)
                return True
    return False

f=open("24game.dat")
file=f.readlines()
nfile=int(file[0])

for i in range(1, nfile+1):
    line=[int(j) for j in file[i].strip().split()]
    #print(line)
    print(DFS(line,0))
    #break
