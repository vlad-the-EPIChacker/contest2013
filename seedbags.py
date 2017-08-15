def adj(x,y):
    r=False
    if x+1<len(rows):
        if rows[y][x+1]=='x':
            rows[y][x + 1] = '.'
            r= True
    if x-1>0:
        if rows[y][x-1]=='x':
            rows[y][x - 1] = '.'
            r = True
    if y+1<len(rows):
        if rows[y+1][x]=='x':
            rows[y+1][x ] = '.'
            r = True
    if y-1>0:
        if rows[y-1][x]=='x':
            rows[y-1][x] = '.'
            r = True
    if x+1<len(rows) and y+1<len(rows):
        if rows[y+1][x+1]=='x':
            rows[y+1][x+1] = '.'
            r = True
    if x-1>0 and y+1<len(rows):
        if rows[y+1][x-1]=='x':
            rows[y + 1][x - 1] = '.'
            r = True
    if x+1<len(rows) and y-1>0:
        if rows[y-1][x+1]=='x':
            rows[y - 1][x + 1] = '.'
            r = True
    if x-1>0 and y-1>0:
        if rows[y-1][x-1]=='x':
            rows[y - 1][x - 1] = '.'
            r = True
    return r

f=open("bags.in")
file=f.readlines()
ncases=int(file[0])
l=1
c=0

while c<ncases:
    ltf = int(file[l])
    rows=[list(file[i].strip()) for i in range(l+1,l+ltf+1)]
    b=0
    for i in range(1,len(rows), 3):
        for ii in range(1, len(rows), 3):
            if adj(ii, i):
                b += 1

    print b
    l += ltf + 1
    c += 1