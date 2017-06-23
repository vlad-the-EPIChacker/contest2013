f=open('drought.dat')
file=f.readlines()
count=int(file[0])

for i in range(1, count+1):
    file[i]=file[i].strip()
    file[i]=file[i].split()

    ave=float(file[i][0])

    y1=file[i][1:13]
    y2=file[i][13:26]

    for ii in range(0, len(y1)):
        y1[ii]  =float(y1[ii])

    for ii in range(0, len(y2)):
        y2[ii]=float(y2[ii])

    sum1=sum(y1)
    sum2=sum(y2)
    if sum1>=ave*2 and sum2>=ave*2:
        print 'drought over'
    elif sum1>=ave and sum2>=ave:
        print 'improving'
    else:
        print 'continuing'
