def convert(n):
    ndigits=len(n)
    n1=int(n)
    s=''
    i=0
    go=True
    if n1==0:
        return con[i]
    if ndigits>2:
        s += con[int(n[i])]
        s +=' '
        s += 'hundred'
        s += ' '
        i += 1
    if ndigits>1:
        if int(n[i]) > 0:
            if int(n[i])==1:
                s += con[int(n)]
                go = False
            else:
                s += con1[int(n[i])-2]
                 s += ' '
        i += 1
    if int(n[i]) > 0 and go:
        s += con[int(n[i])]
    return s




f=open("cosmic.dat")
file=f.readlines()
con=["zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
con1=["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
nfile=int(file[0])

for i in range(1, nfile+1):
    n=file[i].strip()
    n1=int(n)
    n = convert(n)
    while True:
        if n==convert(str(len(n.replace(' ','')))):
            print n,"is cosmic"
            break
        print n, "is", convert(str(len(n.replace(' ',''))))
        n=convert(str(len(n.replace(' ',''))))
    print ''