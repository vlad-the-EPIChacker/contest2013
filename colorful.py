f=open("colorful.dat")
info=f.readlines()
ninfo=info[0]
colors={}

for i in range(1,len(info)):
    x=info[i].split()
    color=x[len(x)-1]
    if not color in colors.keys():
        colors[color]=0
print len(colors.keys())