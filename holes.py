visited=[]

def maxSquare(x,y,squares=0):
    global visited
    if box[y][x]=='#':
        return False,-1
    if (x,y) in visited:
        return False, -2

    #print(x,y)
    visited.append((x,y))
    solutions=[]
    foundPath=False

    cur=maxSquare(x+1,y,squares+1)
    if cur[0]:
        solutions.append(cur)
        foundPath = True
        #print(solutions)

    cur=maxSquare(x-1,y,squares+1)
    if cur[0]:
        solutions.append(cur)
        foundPath = True
        #print(solutions)

    cur=maxSquare(x,y+1,squares+1)
    if cur[0]:
        solutions.append(cur)
        foundPath = True
        #print(solutions)

    cur=maxSquare(x,y-1,squares+1)
    if cur[0]:
        solutions.append(cur)
        foundPath = True
        #print(solutions)

    #cur=(True,sum([i[1] for i in solutions]))
    #solutions.append(cur)

    #print(solutions)
    if not foundPath:
        #print(x, y)
        return True,squares
    if squares==1:
        return True, 1+sum([i[1] for i in solutions])
    return True,sum([i[1] for i in solutions])

f=open('holes.dat')
file=f.readlines()
ncases=int(file[0])
l=1
c=0
while c<ncases:
    dim=file[l].split()
    visited=[]
    h=int(dim[0])
    b=int(dim[1])
    box=[list(file[i].strip()) for i in range(l+1,l+h+1)]
    sections=[]
    for y in range(1,len(box)-1):
        for x in range(1,len(box[0])-1):
            cur=maxSquare(x,y)
            if cur[0]:
                if cur[1]==0:
                    cur=(cur[0],1)
                sections.append(cur)
    s="sections"
    s1="spaces"
    if len(sections)==1:
        s="section"
    if sum([j[1] for j in sections]) == 1:
        s1 = "space"
    print(str(len(sections)),s+',',sum([j[1] for j in sections]),s1)
    l += h + 1
    c += 1