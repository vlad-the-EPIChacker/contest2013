f=open("clues.dat")
file=f.readlines()
clues=''
words=[]

for i in range(0, 10):
    line=file[i].strip()
    clues += line
clues=clues.split()
for i in range(10,len(file)):
    line=file[i].strip()
    words.append(line)
for i in range(0,len(words)):
    final=[]
    word=words[i]
    for ii in range(0,len(clues)):
        match=True
        clue=clues[ii]
        if len(word) == len(clue):
            for iii in range(0, len(clue)):
                if word[iii]=='*':
                    continue
                if word[iii]!=clue[iii]:
                    match=False
                    break
        else:
            match=False
        if match:
            final.append(clue)
    if len(final)==0:
        print 'NO MATCH'
    else:
        print ' '.join(final)