def simplePath(x,y):
    if x==size-1 and y==size-1:
        return True
    if grid[y][x]=='x':
        return False
    if x+1<size:
        grid[y][x]=' '
        if simplePath(x+1,y):
            return True
    if y+1<size:
        grid[y][x]=' '
        if simplePath(x,y+1):
            return True
    return False

f=open("tractorPath01.in")
file=f.readlines()
size=int(file[0])
grid=[[j for j in i.strip()]for i in file[1:]]
if simplePath(0,0):
    print('YES')
else:
    print('NO')