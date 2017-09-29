def TwoSum(nums, target):
    nums=sorted(nums)
    two=[]
    p1 = 0
    p2 = len(nums)-1
    while p1 < p2:
        t = target - nums[p1]
        if t > nums[p2]:
            p1 += 1

        elif t == nums[p2]:
            two.append((nums[p1],nums[p2]))
            p1 += 1
            p2 -= 1

        elif t < nums[p2]:
            p2 -= 1

    return two


print TwoSum([-2,0,2,7,11,15,9],9)
print TwoSum([-2,0,2,7,11,15,9],10000)
print TwoSum([-2,0,2,7,11,15,9],-10000)
print TwoSum([],9)
print TwoSum([2,7],9)
print TwoSum([9],9)
print TwoSum([2,8],9)