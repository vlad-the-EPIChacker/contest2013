f=open("swwap.dat")
file=f.readlines()
w, h=file[0].split()
l=1
origin=[]
new=[]

while l<2 * h:
    l += h