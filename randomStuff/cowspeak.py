f=open("cowspeak.in")
file=f.readlines()
nfile=int(file[0])

for i in range(1, nfile+1):
    letters=[]
    for ii in file[i].strip().split():
        mm=0
        oo=0
        j=0
        while j<len(ii):
            if ii[j]=='M':
                mm+=1
            elif ii[j]=='O':
                oo+=1
            j+=1
        letters.append((chr(int(hex(mm)[2:]+hex(oo)[2:],16))))
    print(''.join(letters))