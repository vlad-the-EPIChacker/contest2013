def check(x,y):

    if grid[y][x]=='#':
        return 0
    maxs=1
    fail=False
    while not fail:
        for y1 in range(0,maxs):
            for x1 in range(0,maxs):
                if y1+y<len(grid) and x1+x<len(grid):
                    if grid[y1+y][x1+x]=='#':
                        return 1 if maxs==1 else maxs-1
                else:
                    return 1 if maxs==1 else maxs-1
        maxs += 1

f=open("pen.in")
file=f.readlines()
nfile=int(file[0])
l=1
for useless in range(0, nfile):
    size=int(file[l])
    grid=[list(file[i].strip()) for i in range(l+1, size+l+1)]

    final=[]
    for y in range(0, size):
        for x in range(0,size):
            final.append(check(x,y))
    print(max(final)**2)

    l += size + 1