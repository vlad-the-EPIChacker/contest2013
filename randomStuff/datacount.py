files=['accounting.dat', 'bank.dat', 'buoyancy.dat', 'cross.dat', 'cursed.dat', 'determined1.dat', 'determined2.dat', 'drought.dat', 'histonum.dat', 'practiceproblem.dat', 'shuffle.dat', 'sineup.dat','splatter.dat']
sum=0
for i in range(0, len(files)):
    f=open(files[i]).readlines()
    n=len(f)
    sum=sum+n

print sum