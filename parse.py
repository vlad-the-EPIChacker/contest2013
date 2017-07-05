f=open("parse.dat")
file=f.readlines()
nfile=int(file[0])
search=['x^2','xy','y^2','x','y','=']

for i in range(1, nfile+1):
    line=file[i].strip()
    final=[]
    for ii in search:
        n=line.find(ii)
        if n==-1:
            final.append('0')
        else:
            iii=n
            s=''
            while True:
                iii += -1
                if line[iii]=='+' or line[iii]=='-':
                    s=line[iii+1:n]
                    sign= '' if line[iii]=='+' else '-'
                    final.append(sign + (s if len(s)>0 else '1'))
                    break
                elif iii<1:
                    final.append('1')
                    break
                else:
                    s += line[iii]
            line=line[n+len(ii):]
    print final