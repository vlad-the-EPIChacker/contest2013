import random

def binary(a):
    if len(a)==0:
        return (None,None,None)
    if len(a)==1:
        return (a[0],None,None)
    l=binary(a[0:len(a)/2])
    r=binary(a[len(a)/2+1:len(a)])
    return (a[len(a)/2],l,r)

def inorder(t,array1):
    if t[1] is not None:
        inorder(t[1], array1)
    if t[0] is not None:
        array1.append(t[0])
    if t[2] is not None:
        inorder(t[2], array1)
    return

def isin(t,n):
    if t is None:
        return False
    if t[0]==n:
        return True
    if t[0]>n:
        return isin(t[1],n)
    if t[0]<n:
        return isin(t[2],n)

def insert(t,n):
    if t is None:
        return (n,None,None)
    if t[0]==n:
        return t
    if t[0]>n:
        return (t[0],insert(t[1],n),t[2])
    if t[0]<n:
        return (t[0],t[1], insert(t[2],n))

def height(t,n):
    if t==None:
        return n
    a=[height(t[1],n+1),height(t[2],n+1)]
    return max(a)


def printLevelOrder(t):
    if t is None:
        return

    queue = []

    queue.append(t)

    while len(queue) > 0:
        print queue[0][0],
        node = queue.pop(0)

        if node[1] is not None:
            queue.append(node[1])

        if node[2] is not None:
            queue.append(node[2])

array1=[]
start=[1,2,3,4,5,6,7]
inorder(binary(start),array1)
print True if array1==start else False

array1=[]
start=[]
inorder(binary(start),array1)
print True if array1==start or (array1==[None] and len(start)==0) else False

array1=[]
start=[1]
inorder(binary(start),array1)
print True if array1==start or (array1==[None] and len(start)==0) else False

array1=[]
start=[1,3]
inorder(binary(start),array1)
print True if array1==start or (array1==[None] and len(start)==0) else False

array1=[]
start=[1,2,3]
inorder(binary(start),array1)
print True if array1==start or (array1==[None] and len(start)==0) else False

array1=[]
start=[-1,2,-3]
inorder(binary(start),array1)
print True if array1==start or (array1==[None] and len(start)==0) else False

start=[1,2,3,4,5,6,7]
tree=binary(start)
if isin(tree, start[1]):
    print True, start[1]
else:
    print False, start[1]

start=[1,2,3,4,5,6,7]
tree=binary(start)
if isin(tree, 8):
    print True, 8
else:
    print False, 8

start=[1,2,3,4,5,6,7]
tree=binary(start)
print tree
print insert(tree,8)

start1=[5,6,7,2,3,1,4]
start=[]
tree=None
print ''
for i in start1:
    print insert(tree,i)
    tree=insert(tree,i)
array1=[]
inorder(tree,array1)
print array1

start=[1,2,3,4,5,6,7]
tree=binary(start)
print tree
print height(tree,0)

start1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
start=[]
tree=None
print ''
for i in start1:
    print insert(tree,i)
    tree=insert(tree,i)
array1=[]
print tree
print height(tree,0)

start1=[2,3,8,4,1,6,5,7,9,10,20,15,19,13,11,12,14,16,15,18,17,1]
start=[]
tree=None
print ''
for i in start1:
    print insert(tree,i)
    tree=insert(tree,i)
array1=[]
inorder(tree,array1)
print tree
print height(tree,0)

start1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
start=[]
tree=None
print ''
for i in start1:
    print insert(tree,i)
    tree=insert(tree,i)
array1=[]
printLevelOrder(tree)