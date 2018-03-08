import math

n=123913091
print(hex(n))
print(int(hex(n),16))

print(math.floor(1.900))
print(math.ceil(1.100))
print(round(1.123139913,5))

a=[{'a':10,'b':3,'c':2},{'a':8,'d':5,'e':2},{'a':34,'b':7,'f':0}]
a.sort(key=lambda x: x['a'])
print(a)

d={'a':10,'b':3,'c':2}
a1=[(k,v) for k,v in d.items()]
a1.sort(key=lambda x: x[1])
print(a1)