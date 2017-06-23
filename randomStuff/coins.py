def comb(sum, i):
    s=[]
    coins=[1, 6, 15 ,25]
    for c in coins:
        if sum==c:
            return [c]
        if sum<c:
            continue
        else:
            sol=comb(sum-c, i+1)
            sol.append(c)
            if len(sol)<len(s) or len(s)==0:
                s=sol
    return s


sum=19


print(comb(sum, 0))