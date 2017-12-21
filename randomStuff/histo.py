f=open("histo.dat")
file=f.readlines()
nfile=int(file[0])

for i in range(1, len(file), 3):
    ndata=int(file[i])
    width=[int(ii) for ii in file[i+1].strip().split()]
    height = [int(ii) for ii in file[i+2].strip().split()]
    s = 2 * sum(width) + height[0] + height[len(height)-1]
    for ii in range(1, len(height)):
        prev=height[ii-1]
        sur=height[ii]
        s += abs(sur-prev)
    print s