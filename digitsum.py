f=open("digitsum.dat")
N=f.readline()
ans=0

for i in range(0, len(N)):
    ans=ans+int(N[i])
print ans 