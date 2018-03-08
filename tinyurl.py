digs=[str(i) for i in range(0,10)] + [chr(ord('A')+i) for i in range(0,26)] + [chr(ord('a')+i) for i in range(0,26)]

def converter(n, b):
    n1=[]
    negative=False
    if n<0:
        negative=True
        n=int(str(n)[1:])
    while int(n):
        n1.append(digs[int(n%b)])
        n = n/b
    if negative:
        n1.append('-')
    n1.reverse()
    return ''.join(n1)

def encode(n):
    s=''
    s += converter(n,len(digs))
    return s

def decode(s):
    n = 0
    while len(s):
        n *= len(digs)
        chr = digs.index(s[0])
        n += chr
        s=s[1:]
    return n

'''
input1=''
while input1!='exit':
    print("\nInput integer:")
    input1=input(">")
    input1=int(input1)
    print("Encoded:",encode(input1))
    print("Decoded:", decode(encode(input1)))
'''

print(decode(encode(11)))
print(decode(encode(1)))
print(decode(encode(2)))
print(decode(encode(123)))



