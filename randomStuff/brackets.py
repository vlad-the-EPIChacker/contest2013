def push(s1,x):
    s1.append(x)

def pop(s1):
    s1=s1[:len(s1)-1]
    return s1

def brackets(s):
    s=list(s)
    s1=[]
    b={'(':')','[':']','{':'}'}
    for i in s:
        if i in b.keys():
            push(s1,i)
        else:
            if len(s1)>0 and b[s1[len(s1)-1]]==i:
                s1=pop(s1)
            else:
                return 'invalid'
    return 'valid' if len(s1)==0 else 'invalid'


print brackets('()]')
print brackets('({[]})')
print brackets('([)]')
print brackets('(){}')
print brackets('){[]}')
print brackets('[]')
