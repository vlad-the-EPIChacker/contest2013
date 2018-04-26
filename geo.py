def longest(r,n1,line):
    terms = [n1]
    #print(r)
    for l in range(0, len(line)):
        if line[l]*r==terms[0]:
            terms.insert(0,line[l])
        elif line[l]==r*terms[len(terms)-1]:
            terms.append(line[l])
    return r, len(terms)


f=open("geo.dat")
file=f.readlines()
nfile=int(file[0])

for i in range(1, nfile+1):
    line=file[i].split()
    line=[int(i) for i in line]
    final=[]
    for j in range(0,len(line)):
        n=line[j]
        for k in range(0,len(line)):
            n1=line[k]
            r = n/n1
            #print(n,n1)
            if int(r)!=r or j==k or r in [g[0] for g in final]:
                continue
            final.append(longest(r,n,line))
    if final==[]:
        print(1)
    else:
        print(max(final,key= lambda x: x[1])[1])
    #print(line)