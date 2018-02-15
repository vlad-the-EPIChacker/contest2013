f=open("goats-0001.in")
file=f.readlines()
dice1=[int(i) for i in file[0].split()]
dice2=[int(i) for i in file[1].split()]
n1=0
n2=0
for i in dice1:
    for ii in dice2:
        if i>ii:
            n1 += 1
        if i==ii:
            n2+=1
n=round((n1+n2/2)/36,5)
print(n)