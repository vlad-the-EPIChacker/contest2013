def roman1(num):
    n=0
    if len(num)==0:
        return 0
    suf=['CM','CD','XC','XL','IX','IV']
    suf1 = [900, 400, 90, 40, 9, 4]
    sin=['I','V','X','L','C','D','M']
    sin1=[1,5,10,50,100,500,1000]
    while len(num)>0:
        found=False
        for i in range(0,len(suf)):
            if num.startswith(suf[i]):
                n += suf1[i]
                num=num[len(suf[i]):]
                found=True
                break
        if not found:
            n += sin1[sin.index(num[0])]
            num = num[1:]
    return n



print roman1('XXXIII')
print roman1('CXLVII')
print roman1('CCCLXV')
print roman1('XCIV')
print roman1('CCLXXXIX')
print roman1('MMMDXLVIII')