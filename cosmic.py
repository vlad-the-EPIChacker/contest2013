import sys

#comment
def convert(n):
    n=n.rstrip('\n')
    num={'0':'','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven',
         '8':'eight','9':'nine','10':'ten','11':'eleven','12':'twelve','13':'thirteen',
         '14':'fourteen','15':'fifteen','16':'sixteen','17':'seventeen', '18':'eighteen',
         '19':'nineteen'}
    num1={'0':'','1':'','2':'twenty','3':'thirty','4':'forty','5':'fifty','6':'sixty','7':'seventy',
          '8':'eighty','9':'ninety'}
    x=[]
    y=''
    for i in range(len(n)-1,-1,-1):
        if i==len(n)-1:
            if i-1>-1 and n[i-1]=='1':
                x.insert(0,num[n[i-1:]])
            else:
                x.insert(0,num[n[i]])
        elif i==len(n)-2:
            x.insert(0,num1[n[i]])
        elif i==len(n)-3:
            x.insert(0,'hundred')
            x.insert(0, num[n[i]])
    for ii in x:
        if ii=='':
            continue
        y=y+' '+ii
    return y.lstrip(' ')

f=open(sys.argv[1])
file=f.readlines()
nfile=int(file[0])

for i in range(1, nfile+1):
    print convert(file[i])