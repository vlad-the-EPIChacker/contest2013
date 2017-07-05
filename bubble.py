def prnt(p):
    for i in range(0, len(p)):
        line=''.join(p[i])
        print line

def check(x, y, rows, char):
    cha1r=rows[y][x]
    n=0
    row=rows[y]
    col=''.join([rows[i][x]for i in range(0, 10)])
    '''
    for i in range(x, len(row)):
        c=row[i]
        if c != char:
            break
        else:
            n += 1
    for i in range(x, -1,-1):
        c=row[i]
        if c != char:
            break
        else:
            n += 1
    for i in range(y, len(col)):
        c=col[i]
        if c != char:
            break
        else:
            n += 1
    for i in range(y, -1,-1):
        c=col[i]
        if c != char:
            break
        else:
            n += 1
    n -= 3
    '''
    return n

f=open("Bubble.dat")
file=f.readlines()
nfile=int(file[10])
rows=[list(file[i].strip()) for i in range(0,10)]



for i in range(11, nfile+11):
    loc=file[i].strip().split()
    loc=[int(loc[ii]) for ii in range(0, len(loc))]
    n=check(loc[1],loc[0],rows)
    if n>2:
        print 'YES',n
    else:
        print 'NO',n