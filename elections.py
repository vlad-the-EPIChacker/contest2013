f=open('elections.dat')
votes=f.readlines()
nvotes=int(votes[0])
nmsvts={}
big=0

for i in range(1, nvotes+1):
    vote=votes[i].replace('\r\n','')
    if vote in nmsvts:
        nmsvts[vote]+=1
    else:
        nmsvts[vote]=1
for i in nmsvts.keys():
    print i,':',nmsvts[i]
    if nmsvts[i]>big:
        big=nmsvts[i]
        key=i
print key,'is your new president!'
