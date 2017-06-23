import sys

f=open("tag.dat")
lines=f.readlines()
ncases=int(lines[0])
l=1
c=1
while True:
    if c>ncases:
        break
    c += 1
    nl=int(lines[l])
    tags=[]
    for i in range(l, nl+1+l):
        line=lines[i].strip().split()
        tags.append(line)
    l += nl+1
    tags=tags[1:]
    jail={}
    alive=[]
    dead=[]
    invalid=False
    for i in range(len(tags)):
        line=tags[i]
        tagger=line[0]
        tagged=line[2]
        if tagger in dead or tagged in dead or tagger==tagged:
            print "INVALID GAME"
            invalid=True
        if tagger not in alive:
            alive.append(tagger)
        if tagger not in jail.keys():
            jail[tagger]=[]
        jail[tagger].append(tagged)
        if tagged in alive:
            alive=[ii for ii in alive if ii!=tagged]
        if tagged in jail.keys():
            for ii in (jail[tagged]):
                alive.append(ii)
                dead = [iii for iii in dead if iii != ii]
        dead.append(tagged)
        jail[tagged]=[]
    if not invalid:
        if len(alive)>1:
            print 'VALID GAME'
            print 'Unfinished'
        else:
            print 'VALID GAME'
            print alive[0]
    print ''
