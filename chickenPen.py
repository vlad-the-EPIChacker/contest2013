import math

def size(n):
    q=1
    while n>q**2:
        q+=1
    return q

def size1(n):
    a=int(n**0.5)
    return a+1 if a**2<n else a

f=open("chickenPen04.in")
n1=int(f.readlines()[0])
n=size1(n1)
prnt=['#'*(n+2)]

for i in range(0, n):
    prnt.append('#%s#' % ('.'*n))
prnt.append(prnt[0])
for i in prnt:
    print(i)