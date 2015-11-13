f=open("nucleotides.dat")
DNA=f.readline()
def dostuff():
    counter=0
    count2=0
    letter=0
    letter2=0
    nuc=''.join(sorted(DNA))

    for i in range(0,len(nuc)):
        if i==0:
            letter=nuc[0]
            counter=1
        elif nuc[i]==nuc[i-1]:
            counter += 1

        else:
            if count2<counter:
                count2=counter
                letter2=letter

            counter=1
            letter=nuc[i]

    if count2<counter:
            count2=counter
            letter2=letter
    print letter2, ':', count2
def WUZZAP():
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
#WUZZAP()
dostuff()