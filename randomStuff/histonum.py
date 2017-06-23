import sys

f=open(sys.argv[1])
file=f.readlines()
sum=''
smashtable={}
smashtable['0']=0
smashtable['1']=0
smashtable['2']=0
smashtable['3']=0
smashtable['4']=0
smashtable['5']=0
smashtable['6']=0
smashtable['7']=0
smashtable['8']=0
smashtable['9']=0

for i in range(0, len(file)):
    x=file[i].strip()
    sum=sum+x
sum=list(sum)
for i in range(0, len(sum)):
    smashtable[str(sum[i])]+=1
for i in range(0, 9):
    n=smashtable[str(i)]
    if n!=0:
        print str(i)+'|'+'*'* n, '{'+str(n)+'}'
