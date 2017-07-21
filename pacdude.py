def pacdude(n):
    char=rows[n[1]][n[0]]
    if char=='#':
        return False
    if char=='G':
        return False
    if char==' ':
        return False
    if char=='X':
        rows[n[1]][n[0]]='O'
        return True
    if char=='.':
        rows[n[1]][n[0]]=' '
    if n[0]+1<dim[0]:
        if pacdude([n[0]+1,n[1]]):
            return True


    if n[0]-1>-1:
        if pacdude([n[0]-1,n[1]]):
            return True

    if n[1]+1<dim[1]:
        if pacdude([n[0],n[1]+1]):
            return True

    if n[1]-1>0:
        if pacdude([n[0],n[1]-1]):
            return True
    rows[n[1]][n[0]] = '.'
    return False

f=open("pacdude.dat")
file=f.readlines()
nfile=int(file[0])

c=0
l=1

while c<nfile:
    dim=file[l].strip().split()
    dim=[int(dim[i]) for i in range(0,len(dim))]
    grid=[list(file[i].strip()) for i in range(l+1,l+dim[1]+1)]
    for i in range(0, len(grid)):
        if ''.join(grid[i]).find('O')>-1:
            n=[''.join(grid[i]).find('O'),i]
    rows=grid
    rows[n[1]][n[0]]='.'
    out=pacdude(n)
    if not out:
        print "UH-OH!"
    else:
        print "NOM-NOM!"
        for i in range(0,len(grid)):
            print ''.join(grid[i])
    c+=1
    l+=dim[1]+1
    print ''