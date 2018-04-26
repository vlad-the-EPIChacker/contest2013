import math

f=open("factor.dat")
file=f.readlines()
nfile=int(file[0])

for i in range(1,nfile+1):
    line=file[i].strip().split()
    orders={}
    orders["x^2"]=0
    orders["x^1"] = 0
    orders["x^0"] = 0
    terms=[line[0]]

    #print(line)
    for ii in range(1,len(line),2):
        sign=line[ii]
        #print(sign)
        if sign=='-':
            line[ii+1]='-'+line[ii+1]
        terms.append(line[ii+1])
    #print(line)
    #print(terms)



    for ii in range(0,len(terms)):
        term=terms[ii]
        #print(term)
        x=term[len(term)-3:]
        cof=term[:len(term)-3]
        #print(x,cof)
        orders[x] += int(cof)



    a=orders["x^2"]
    b=orders["x^1"]
    c=orders["x^0"]
    #print(a,b,c)
    der=(b**2) - (4 * a * c)
    #print(b**2)
    #print(4 * a * c)
    #print(der)
    if a==0:
        if c==0:
            print(0)
        elif b==0:
            print(None)
        else:
            #print(a,b,c)
            print(int(-1 * (c / b)))

    elif der < 0:
        print(None)

    elif der ==0:
        if b==0:
            print(0)
        else:
            print((-1 * b) / (2 * a))

    else:
        t1= (-b + (der ** 0.5)) / (2*a)
        t2= (-b - (der ** 0.5)) / (2*a)
        t3=[t1,t2]
        t3.sort()
        print(t3)