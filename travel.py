def DFS(cur,path=[],cost=0):
    if cur==end:
        return cost
    if cur in path:
        return -1
    final=[]
    x=cur[0]
    y=cur[1]
    chr=field[y][x]
    if chr == '#':
        return -1
    #print(chr)
    if 0<=x+1<sizex:
        sol=DFS((x+1,y),path + [cur],cost+costs[chr])
        if sol>-1:
            final.append(sol)
    if 0<=x-1<sizex:
        sol=DFS((x-1,y),path + [cur],cost+costs[chr])
        if sol>-1:
            final.append(sol)
    if 0<=y+1<sizey:
        sol=DFS((x,y+1),path + [cur],cost+costs[chr])
        if sol>-1:
            final.append(sol)
    if 0<=y-1<sizey:
        sol=DFS((x,y-1),path + [cur],cost+costs[chr])
        if sol>-1:
            final.append(sol)
    if final==[]:
        return -1
    return min(final)


costs={}
costs['D']=2.0
costs['R']=10.0
costs['M']=5.0
costs['S']=10/2.5
costs['P']=0
costs['C']=0

f=open("travel.dat")
file=f.readlines()
ncases=int(file[0])
l=1
c=0
while c<ncases:
    sizex, sizey=int(file[l].split()[0]), int(file[l].split()[1])
    field=[list(i.strip()) for i in file[l+1:l+sizey+1]]
    for i in field:
        if 'P' in i:
            start  = (i.index('P'),field.index(i))
        if 'C' in i:
            end  = (i.index('C'),field.index(i))
    #print(sizex,sizey)
    #print(field)
    #print(start)
    #print(end)
    print(DFS(start))

    l += sizey + 1
    c += 1
