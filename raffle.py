fd=open('raffle.dat')
raffles=fd.readlines()
nraffles=int(raffles[0])
big=0
big2=0

for i in range(1, nraffles+1):
    raf=int(raffles[i])
    if raf>big:
        big2=big
        big=raf
print big2