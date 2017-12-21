def findKey(v):
    for i in causes.keys():
        if causes[i]==v:
            return i
    return False

f=open("deer.dat")
file=f.readlines()
deer={}
causes={"ALIVE":0,"COYOTE":0,"MOUNTAIN LION":0,"BEAR":0,"NATURAL CAUSES":0}

for i in file:
    i=i.strip()
    if len(i[12:])==0:
        deer[i[0:4]]='ALIVE'
    else:
        deer[i[0:4]]=i[12:]

sum=len(deer.keys())
for i in deer.keys():
    causes[deer[i]] += 1

for i in reversed(sorted(causes.values())):
    causes[i]=str(int(round(causes[findKey(i)]/float(sum),2)*100))+'%'
    print findKey(i)+' '+causes[i]