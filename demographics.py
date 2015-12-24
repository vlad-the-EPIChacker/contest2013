f=open('demographics.dat')
data=f.readlines()
ndata=int(data[0])
info={}
ave=0
final={}
town=0

for i in range(1,ndata+1):
    focus=data[i].split()
    if not focus[1] in info.keys():
        info[focus[1]]=[]
    info[focus[1]].append(float(focus[2]))
for key in info.keys():
    ave=0
    for ii in info[key]:
        ave += ii
    ave=ave/len(info[key])
    final[key]=ave
small=final[final.keys()[0]]
for iii in final.keys():
    if final[iii]<small:
        small=final[iii]
        town=iii
print town ,':', small