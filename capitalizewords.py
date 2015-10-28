fd=open('capitalizewords.dat')
sentence=fd.readlines()
words=sentence[0].split()
n=int(sentence[1])
prnt=''

for i in range(0, len(words)):
    if i<n:
        prnt=prnt+' '+words[i].upper()
    else:
        prnt=prnt+' '+words[i]
print prnt