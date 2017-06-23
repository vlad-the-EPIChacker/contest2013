f=open("elections.dat")
file=f.readlines()
nfile=int(file[0])
names={}

for i in range(1, nfile+1):
    name=file[i].strip()
    if name not in names.keys():
        names[name]=0
    names[name]+=1
abc=sorted(names.keys())
big=[0,'']
for i in abc:
    if names[i]>big[0]:
        big[0]=names[i]
        big[1]=i
    print i+':',names[i]
print big[1],'is your new president!'
