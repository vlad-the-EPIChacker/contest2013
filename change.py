def weird(ch,count):
    if ch==0:
        return (True,[i for i in count])
    if ch<0:
        return (False,[])
    min1=[]
    bool=False
    for i in coins:
        new=weird(ch-i,count)
        if new[0]:
            if len(min1)==0:
                min1=new[1]
                min1.append(i)
                bool = True
            elif len(min1)>len(new[1]):
                min1=new[1]
                min1.append(i)
                bool = True
    return (bool,min1)

f=open("weirdChange.dat")
file=f.readlines()
nfile=int(file[0])
coins=[1,5,13,23,37,47]

for i in range(1, nfile+1):
    change=int(file[i])
    s='$'+str(change*3/100)+'.'
    if len(str((change*3)%100))==1:
        s += '0'+str((change*3)%100)
    else:
        s += str((change * 3) % 100)
    print weird(change,[])

