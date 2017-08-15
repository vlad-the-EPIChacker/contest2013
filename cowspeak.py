f=open("cowspeak.in")
file=f.readlines()
nfile=int(file[0])

for i in range(1, nfile+1):
    line=file[i].strip().split()
    s=''
    for ii in range(0, len(line)):
        phrase=line[ii]
        n=hex(phrase.count('M')+phrase.count('O'))
        print n
    print s