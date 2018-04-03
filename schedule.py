def schedule(node,classes,visited,sched):
    if node in visited:
        return
    if node in classes.keys():
        for child in classes[node]:
            schedule(child,classes,visited,sched)
    visited.append(node)
    sched.append(node)


classesInput=[('1','9'),('1','4'),('4','6'),('4','7'),('2','4'),('2','5'),('5','8'),('3','5')]
classes={}
first=[]
for i in classesInput:
    k=i[0]
    if k in classes:
        classes[i[0]].append(i[1])
    else:
        classes[i[0]]=[i[1]]


for k in classes.keys():
    firstBool=True
    for children in classes.values():
        if k in children:
            firstBool=False
    if firstBool:
        first.append(k)

s=[]
v=[]
for i in first:
    schedule(i,classes,v,s)
s.reverse()
print(classes)
print(s)