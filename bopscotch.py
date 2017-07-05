f=open("bopscotch.dat")
file=f.readlines()
nfile=int(file[0])



for ii in range(1, nfile+1):
    n=int(file[ii])
    i = 0
    l = 0
    map = []
    while i<n:
        st=''
        if i==0:
            st='\\ '+str(i+1)+' /'
        elif i==n-1:
            st='/ '+str(n)+' \\'
        elif n%3==1 and i==n-2:
            st = ' [' + str(i + 1) + ']'
        elif l%2==0:
            i += 1
            st='['+str(i)+']['+str(i+1)+']'
        else:
            st=' ['+str(i+1)+']'
        map.append(st)
        i += 1
        l += 1
    map = map[::-1]
    for iii in range(0, len(map)):
        print map[iii]
    print ''