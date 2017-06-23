f=open('shuffle.dat')
file=f.readlines()


for i in range(0, len(file)):
    words = {}
    file[i]=file[i].strip().split()

    for ii in range(0, len(file[i])):
        words[file[i][ii]]=0

    print ' '.join(sorted(words.keys()))