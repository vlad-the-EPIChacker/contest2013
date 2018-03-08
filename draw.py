f=open("draw.dat")
file=f.readlines()
nfile=int(file[0])

for j in range(1, nfile+1):
    line=file[j].strip()
    if line.find('rectangle') > -1:
        r = int(line.split()[1])
        c = int(line.split()[2])
        hollow=False
        if line.split()[3]=='n':
            hollow=True
        if hollow:
            print('#' * c)
            for i in range(0, r-2):
                print('#%s#' % (' '*(c-2)))
            print('#' * c)
        else:
            for i in range(0, r):
                print('#' * c)

    elif line.find('left triangle') > -1:
        l=int(line.split()[2])
        hollow = False
        if line.split()[3] == 'n':
            hollow = True
        if hollow:
            print('#')
            for i in range(0,l-2):
                print('#%s#' % (' ' * i))
            print('#' * l)
        else:
            print('#')
            for i in range(0, l - 2):
                print('#'*(i+2))
            print('#' * l)

    elif line.find('right triangle') > -1:
        l = int(line.split()[2])
        hollow = False
        if line.split()[3] == 'n':
            hollow = True
        if hollow:
            print(' '*(l-1)+'#')
            for i in range(0,l-2):
                print(' ' *(l-i-2) + '#%s#' % (' ' * i))
            print('#' * l)
        else:
            print(' ' * (l - 1) + '#')
            for i in range(0, l - 2):
                print(' ' * (l - i - 2) + '#'*(i+2))
            print('#' * l)
    elif line.find('diamond') > -1:
        l = int(line.split()[1])
        hollow = False
        if line.split()[2] == 'n':
            hollow = True
        l=l-2
        if hollow:
            print(' '*int((l/2)+1)+'#')
            for i in range(0, int(l/2)):
                s=''
                s += ' '*(int(l/2)-i)
                s += '#'*(int(2*i+3))
                print(s)
            for i in range(int(l/2),-1,-1):
                s=''
                s += ' '*(int(l/2)-i)
                s += '#'*(int(2*i+3))
                print(s)
            print(' ' * int((l / 2)+1) + '#')
        else:
            print(' '*int((l/2)+1)+'#')
            for i in range(0, int(l/2)):
                s=''
                s += ' '*(int(l/2)-i)
                s += '#'
                s += ' ' * (int(2 * i + 1))
                s += '#'
                print(s)
            for i in range(int(l/2),-1,-1):
                s=''
                s += ' '*(int(l/2)-i)
                s += '#'
                s += ' ' * (int(2 * i + 1))
                s += '#'
                print(s)
            print(' ' * int((l / 2)+1) + '#')