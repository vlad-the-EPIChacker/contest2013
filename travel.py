class PQueue():
    def __init__(self):
        self.list = []

    def pop(self):
        v=self.list[0]
        self.list = self.list[1:]
        return v

    def push(self,v): #v is a tuple-> (value,priority)
        self.list.append(v)
        self.list.sort(key=lambda x: x[1])

    def notEmpty(self):
        return len(self.list)>0

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

def BFS(cur,end):
    q = PQueue()
    q.push((cur,0))
    visited={cur:1}
    while q.notEmpty():
        temp=q.pop()
        if temp[0]==end:
            return temp[1]
        x=temp[0][0]
        y=temp[0][1]
        curcost=temp[1]
        if 0 <= x + 1 < sizex and field[y][x+1]!='#':
            a=(x+1, y)
            if a not in visited.keys():
                visited[a] = 1
                price=costs[field[y][x+1]]+curcost
                q.push((a,price))

        if 0 <= x - 1 < sizex and field[y][x-1]!='#':
            a=(x-1, y)
            if a not in visited.keys():
                visited[a] = 1
                price=costs[field[y][x-1]]+curcost
                q.push((a,price))

        if 0 <= y +1  < sizey and field[y+1][x]!='#':
            a=(x, y+1)
            if a not in visited.keys():
                visited[a] = 1
                price=costs[field[y+1][x]]+curcost
                q.push((a,price))

        if 0 <= y -1  < sizey and field[y-1][x]!='#':
            a=(x, y-1)
            if a not in visited.keys():
                visited[a] = 1
                price=costs[field[y-1][x]]+curcost
                q.push((a,price))




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

#q = PQueue()
#q.push((3, 8))
#q.push((1, 3))
#print(q.pop())
#print(q.pop())

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
    #print(DFS(start))
    print(BFS(start,end))

    l += sizey + 1
    c += 1
