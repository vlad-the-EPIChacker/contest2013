f=open("digitsearch.dat")
file=f.readlines()
nfile=int(file[0])

for i in range(1,nfile+1):
    ints=[]
    line=file[i].strip()
    for i in line:
        try:
            int(i)
            ints.append(int(i))
        except (Exception, ArithmeticError) as e:
            pass
    print(ints)
    for ii in range(1,len(ints)):
        n1=ints[ii-1]
        n=ints[ii]
        if n-n1!=1 or n-n1!=0:
            print(n1)
            break
    #print(line)