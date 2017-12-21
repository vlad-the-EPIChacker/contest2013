def check(s, s1):
    if len(s)!=len(s1):
        return False
    for i in range(0,len(s)):
        if s[i]!=s1[i] and s1[i]!='*':
            return False
    return True

f=open("crosswardclues.dat")
file=f.readlines()
words=' '.join(file[:10])
words=words.split()
print words

for i in range(11, len(file)):
    final=[]
    for ii in words:
        if check(ii.strip(),file[i].strip()):
            final.append(ii)
    print ' '.join(final)