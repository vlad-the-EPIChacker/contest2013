f=open("lines.dat")
file=f.readlines()
nfile=int(file[0])

for i in range(1, nfile+1):
    line=file[i].strip().split()
    #print(line)
    m=int(line[0])
    b=int(line[1])
    m1=int(line[2])
    b1=int(line[3])
    if m1==m:
        print(None)
    else:
        x=int((b-b1)/(m1-m))
        y=int(m*x+b)
        print(x,y)