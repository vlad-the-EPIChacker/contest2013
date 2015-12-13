def if_WIN(n):
    if n==7 or n==11 or n==15 or n==20:
        return True
    return False
def if_LOSE(n):
    if n==2 or n==3 or n==10 or n==13 or n==19:
        return True
    return False

def middle(n, sn):
    if n==7 or n==10 or n==11 or n==15:
        return -1
    if sn==n:
        return 1
    return 0

f=open('dico.dat')
data=f.readlines()
ndata=int(data[0])
result=None

for i in range(1, ndata+1):
    result=None
    ii=0
    narray=data[i].split()
    for ii in range(0, len(narray)-1):
        n=int(narray[ii])
        if ii==0:
            sn=n
            if if_WIN(n):
                result=('WIN', 1)
                break
            elif if_LOSE(n):
                result=('LOSS', 1)
                break
        else:
            if middle(n,sn)==1:
                result=('WIN', ii+1)
                break
            if middle(n,sn)==-1:
                result=('LOSS', ii+1)
                break
    if not result==None:
        print result[0], result[1]
    else:
        print 'NO RESULT', len(narray)-1