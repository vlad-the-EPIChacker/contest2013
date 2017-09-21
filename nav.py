def tools(x,y):
  #  pm()
    chr=map[y][x]
  #  print(chr)
    if chr=='X':
        return True
    if chr not in t:
        return False
    map[y][x]='P'

    if x+1<len(map):
        if tools(x+1,y):
            return True
    if x -1 > -1:
        if tools(x-1,y):
            return True

    if y +1 < len(map):
        if tools(x,y+1):
            return True
    if y-1 > -1:
        if tools(x,y-1):
            return True

    map[y][x]=chr
    return False

def pm():
    for i in map:
        print ''.join(i)
    print ''

f=open("nav.dat")
file=f.readlines()
ncases=int(file[0])
c=0
l=1

while c<ncases:
    prnt=False
    t = ['.']
    x=123
    ln=int(file[l])
    loc=[]
    map=[list(file[i].strip()) for i in range(l+1, ln+l+1)]

    for i in range(0, len(map)):
        if ''.join(map[i]).find('S')>-1:
            loc=[''.join(map[i]).find('S'), i]
            map[loc[1]][loc[0]]='.'

    t1 = ['R', 'B', 'G']

    if tools(loc[0],loc[1]):
        print '0'
        prnt=True




    for i in t1:
        t.append(i)
        #print t
        if tools(loc[0], loc[1]):
            if not prnt:
                print '1'
                prnt = True
        map = [list(file[iii].strip()) for iii in range(l + 1, ln + l + 1)]
        map[loc[1]][loc[0]] = '.'
        t = ['.']

    for i in range(0,len(t1)):
        t.append(t1[i])
        for ii in t1:
            if ii not in t:
                t.append(ii)
                #print t
                if tools(loc[0], loc[1]):
                    if not prnt:
                        print '2'
                        prnt=True
            map = [list(file[iii].strip()) for iii in range(l + 1, ln + l + 1)]
            map[loc[1]][loc[0]] = '.'
            t=['.',t1[i]]
        t=['.']

    map = [list(file[i].strip()) for i in range(l + 1, ln + l + 1)]
    t=['.']
    map[loc[1]][loc[0]] = '.'

    t=['.',t1[0],t1[1],t1[2]]
    if tools(loc[0],loc[1]):
        if not prnt:
            print '3'
            prnt=True
    map = [list(file[i].strip()) for i in range(l + 1, ln + l + 1)]
    t=['.']
    map[loc[1]][loc[0]] = '.'





#    print x
    l += ln +1
    c += 1