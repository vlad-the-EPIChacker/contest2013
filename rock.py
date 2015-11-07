def decide1(throw):
    ops={'ROCK':{'SCISSORS':'YOU WIN', 'PAPER':'YOU LOSE', 'ROCK': 'TIE'},
         'PAPER':{'SCISSORS':'YOU LOSE', 'PAPER':'TIE', 'ROCK': 'YOU WIN'},
         'SCISSORS':{'SCISSORS':'TIE', 'PAPER':'YOU WIN', 'ROCK': 'YOU LOSE'}}

    return (ops[throw[0]])[throw[1]]
def decide(throw):
    if throws[0]=='ROCK':
        if throws[1]=='PAPER':
            print throws, 'YOU LOSE'
        if throws[1]=='SCISSORS':
            print throws, 'YOU WIN'
        else:
            print throws, 'TIE'
    if throws[0]=='SCISSORS':
        if throws[1]=='PAPER':
            print throws, 'YOU WIN'
        if throws[1]=='ROCK':
            print throws, 'YOU LOSE'
        else:
            print throws, 'TIE'
    if throws[0]=='PAPER':
        if throws[1]=='ROCK':
            print throws, 'YOU WIN'
        if throws[1]=='SCISSORS':
            print throws, 'YOU LOSE'
        else:
            print throws, 'TIE'
f=open("rock.dat")
data=f.readlines()
ndata=data[0]

for i in range(1, len(data)):
    throws=data[i].split()
    print throws[0], throws[1], decide1(throws)
