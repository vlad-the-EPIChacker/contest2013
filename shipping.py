f=open("shipping.in")
file = f.readlines()
nfile = int(file[0])
l = 1

for i in range(0, nfile):
    n = 0
    nstuff = int(file[l])
    stuff = file[l+1:l+nstuff+1]
    for j in stuff:
        temp = j.split()
        n += int(temp[1]) * float(temp[2])
    print('$%s' % (str(n) if n==round(n,2) else str(n)+'0'))
    l += nstuff + 1
