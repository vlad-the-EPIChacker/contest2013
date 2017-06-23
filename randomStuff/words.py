f=open("words.dat")
lines=f.readlines()
nwords=int(lines[0])
words=[]
hor=[]
ver=[]

for i in range(1, nwords+1):
    line=lines[i].strip()
    words.append(line)
hor=[''.join(lines[i].strip().split()) for i in range(nwords+1,nwords+11)]
for x in range(0,len(hor)):
    col=''
    for y in range(0, len(hor)):
        char=hor[y][x]
        col += char
    ver.append(col)


for word in words:
    for ii in range(0,len(hor)):
        row=hor[ii]
        sol=row.find(word)
        if sol>-1:
            print sol,ii
            continue
    for ii in range(0,len(hor)):
        row=ver[ii]
        sol=row.find(word)
        if sol>-1:
            print ii, sol
            continue
