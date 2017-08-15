pos=[]

def queens(y):
    global pos
    if len(pos)==8 and y<9:
        print pos
        pos = pos[:len(pos) - 1]
        return
    for x in range(0, 8):
        if not collide(x, y):
            pos.append((x, y))
            queens(y+1)
            pos = pos[:len(pos) - 1]



def collide(x1,y1):
    for i in pos:
        x2 = i[0]
        y2 = i[1]
        if x1 == x2:
            return True
        if y1 == y2:
            return True
        if abs(x1-x2) == abs(y1-y2):
            return True
    return False


queens(0)
