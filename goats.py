f=open("goats.dat")
dices=f.readlines()
dice1=dices[0].strip().split()
dice2=dices[1].strip().split()
win=0


for i in range(0, 6):
    for ii in range(0, 6):
        if dice1[i] > dice2[ii]:
            win += 1

s=str(round(win/36.0 , 5))
s += '0'*(7-len(s))
print s
