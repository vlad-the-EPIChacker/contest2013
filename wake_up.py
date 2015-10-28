fd=open('wakeup.dat')
words=fd.readlines()
word=words[0]
days=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
x=False

for i in range(0,len(days)):
    if word==days[i]:
        x=True
        print 'Wake up, it''s', days[i]+'!'
        break
if x==False:
    print 'Relax, it''s', word+'!'