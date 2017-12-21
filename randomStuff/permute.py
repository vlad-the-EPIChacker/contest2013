def recursive(s):
    if len(s)==0:
        return 'yes'
    for ii in elements:
        if s.find(ii)==0:
            if recursive(s[len(ii):])=='yes':
                return 'yes'
    return 'no'

f=open("permute.dat")
file=f.readlines()
nfile=int(file[4])
elements=[]

for i in range(0, 4):
    for ii in file[i].strip().split():
        elements.append(ii.lower())

for i in range(5, nfile+5):
    line=file[i].strip()
    print recursive(line)