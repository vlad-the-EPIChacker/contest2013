f=open("over.dat")
file=f.readlines()
nfile=int(file[0]);

for i in range(1, nfile+1):
    line=file[i].strip().split()
    line=[int(line[i]) for i in range(0, len(line))]
    pay=0
    if sum(line)>40:
        pay += (sum(line)-40)*4
    for ii in range(0, len(line)):
        mult=10
        hour=line[ii]
        if ii==0:
            mult=15
        if ii==6:
            mult=20
        pay += hour * mult
        if hour>8:
            pay += (hour-8)*2

    pay=int(pay)
    print '$'+str(pay)