f=open("wimbledon.dat")
file=f.readlines()
nfile=int(file[0])
convert=['love','one','two','three','four','five','six','seven','eight','nine']

for i in range(1, nfile+1):
    line=[int(ii) for ii in file[i].strip().split('-')]
    found=True
    if line[0]==line[1] and found:
        print convert[line[0]], "all"
    elif line[0]>5 and line[0]-line[1]>1:
        print "set"
    elif line[1]>5 and line[1]-line[0]>1:
        print "set"
    else:
        print convert[line[0]], '-', convert[line[1]]