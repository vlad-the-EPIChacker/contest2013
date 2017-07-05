f=open("cardsort.dat")
file=f.readlines()
nfile=int(file[0])
nums={}
nums['K']=13
nums['Q']=12
nums['J']=11
nums['A']=1
nums[13]='K'
nums[12]='Q'
nums[11]='J'
nums[1]='A'

for i in range(1, nfile+1):
    line=file[i].strip().split(', ')
    line=[line[ii].split() for ii in range(0, len(line))]
    for ii in range(0, len(line)):
        if line[ii][1] in nums.keys():
            line[ii][1]=nums[line[ii][1]]
        else:
            line[ii][1]=int(line[ii][1])
    line1=[line[ii] for ii in range(0, len(line)) if line[ii][0]=='club']
    line2 = [line[ii] for ii in range(0, len(line)) if line[ii][0] == 'heart']
    line3 = [line[ii] for ii in range(0, len(line)) if line[ii][0] == 'diamond']
    line4 = [line[ii] for ii in range(0, len(line)) if line[ii][0] == 'spade']
    line1 = sorted(line1, key=lambda x: x[1])
    line2 = sorted(line2, key=lambda x: x[1])
    line3 = sorted(line3, key=lambda x: x[1])
    line4 = sorted(line4, key=lambda x: x[1])
    line=[]
    for ii in range(0, len(line1)):
        line.append(line1[ii])
    for ii in range(0, len(line3)):
        line.append(line3[ii])
    for ii in range(0, len(line2)):
        line.append(line2[ii])
    for ii in range(0, len(line4)):
        line.append(line4[ii])
    for ii in range(0, len(line)):
        if line[ii][1] in nums.keys():
            line[ii][1]=nums[line[ii][1]]
        else:
            line[ii][1]=str(line[ii][1])
        line[ii]=line[ii][0]+' '+line[ii][1]
    prnt=''
    for ii in range(0, len(line)):
        prnt += line[ii]
        prnt += ', '
    prnt = prnt[:len(prnt)-2:]
    print prnt
    print ''