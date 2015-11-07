f=open("nucleotides.dat")
DNA=f.readline()
nucs={}
big=0

for i in range(0, len(DNA)):
    nuc=DNA[i]
    if not nuc in nucs.keys():
        nucs[nuc]=1
    else:
        nucs[nuc]+=1
for key in nucs.keys():
    n=nucs[key]
    if n>big:
        big=n
for key in nucs.keys():
    if nucs[key]==big:
        print key,':',nucs[key]