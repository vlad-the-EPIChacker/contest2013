def mix(array):
    if len(array)<k+1:
        array=sorted(array)
        if array not in salads:
            salads.append(array)
        return
    for ii in array:
        mix([iii for iii in array if iii != ii])

f=open("fruitsalad.dat")
file=f.readlines()
nfile=int(file[0])
k=3

for i in range(1,nfile+1):
    fruits=file[i].strip().split()
    salads=[]
    mix(fruits)
    salads=sorted(salads)
    for ii in salads:
        print ' '.join(ii)
    print ''
