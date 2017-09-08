def small(l):
    small=l[0]
    for i in l:
        if i[0]<small[0]:
            small=i
    return small

f=open("overbooked.dat")
file=f.readlines()
nfile=int(file[0])

for i in range(1, 2*(nfile),2):
    n=int(file[i])
    line=file[i+1].strip()
    line=[ii.strip('()') for ii in line.split(") (")]
    line = [[[int(iiii) for iiii in iii.split(':')] for iii in ii.split(", ")] for ii in line]
    line=[[iii[0]*60+iii[1] for iii in ii] for ii in line]
    scech=[]
    scech.append(small(line))
    line = [ii for ii in line if ii != small(line)]
    while len(line)>0 and sum([ii[1]-ii[0] for ii in scech])<24*60:
        if small(line)[0]>scech[len(scech)-1][1]:
            scech.append(small(line))
        line = [ii for ii in line if ii != small(line)]
    scech=scech[:len(scech)]
    final=[]
    for ii in scech:
        s='('
        for iii in ii:
            n1=str(iii/60)
            n2=str(iii%60)
            if len(n1)<2:
                n1='0'+n1
            if len(n2)<2:
                n2='0'+n2
            s += n1+':'+n2
            s += ', '
        s = s[:len(s)-2]
        s+=')'
        final.append(s)
    print ' '.join(final)
    print ''