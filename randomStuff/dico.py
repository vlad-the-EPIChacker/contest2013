f=open("dico.dat")
file=f.readlines()
nfile=int(file[0])
win=['7', '11', '15', '20']
lose=['2','3','10','13','19']
result=False

for i in range(1,nfile+1):
    result=False
    line=file[i].strip().split()
    n=line[0]
    n1=line[1]
    i=1
    if n in win and not result:
        print 'WIN 1'
        result=True
    if n in lose and not result:
        print 'LOSS 1'
        result=True
    while True:
        n1=line[i]
        if n1=='0':
            break
        if n1 in win and not result:
            print 'LOSS',i+1
            result=True
        if n1==n and not result:
            print 'WIN',i+1
            result=True
        i += 1
    if not result:
        print 'NO RESULT',i+1

