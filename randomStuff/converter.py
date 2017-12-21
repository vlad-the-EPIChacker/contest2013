import string
digs = string.digits + string.letters

def converter(n, b):
    n1=[]
    negative=False
    if n<0:
        negative=True
        n=int(str(n)[1:])
    while n:
        n1.append(digs[n%b])
        n = n/b
    if negative:
        n1.append('-')
    n1.reverse()
    return ''.join(n1)


print converter(-4,2)
print converter(10240000,16)
print converter(-4,2)
print converter(-4,2)