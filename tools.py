nogo=[]
tools=[]
op=9999999999999999999

def dig(x,y):
    global op
    rm=False
    if len(tools)>=op:
        return op
    if grid[y][x]=='X':
        op=len(tools)
        return len(tools)
    if grid[y][x] not in tools and grid[y][x]!='S' and grid[y][x]!=' '  and grid[y][x]!='.':
        tools.append(grid[y][x])
        rm=True
    final=[]
    chr=grid[y][x]
    grid[y][x] = ' '
    if x+1<len(grid) and grid[y][x+1]!=' ':
        final.append(dig(x+1,y))
    if x-1>=0 and grid[y][x-1]!=' ':
        final.append(dig(x-1,y))
    if y+1<len(grid) and grid[y+1][x]!=' ':
        final.append(dig(x,y+1))
    if y-1>=0 and grid[y-1][x]!=' ':
        final.append(dig(x,y-1))
    grid[y][x] = chr
    if rm:
        tools.remove(grid[y][x])
    if len(final) ==0:
        return op
    op=min(final)
    return min(final)

f=open("tools.dat")
file=f.readlines()
ncases=int(file[0])
l=1
c=0
while c<ncases:
    tools=[]
    op=9999999999999999999
    side=int(file[l])
    grid=[list(i.strip()) for i in file[l+1:l+side+1]]
    for i in grid:
        if 'S' in i:
            start=(i.index('S'),grid.index(i))
    print(dig(start[0],start[1]))
    l += side + 1
    c += 1