def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    pt1=0
    l_nums=len(nums)
    pt2=l_nums//2
            
    while target!=nums[pt2] and pt1!=pt2:
        if target<nums[pt2]:
            l_nums=pt2
            pt2=pt1+(pt2-pt1)//2             
        else:
            pt1=pt2
            pt2=l_nums-1
        print(pt1,pt2)
    if target==nums[pt2]:
        return pt2
    elif target>nums[pt2]:
        return pt2+1
    else:
        return 0

nums = [1,3,5,6]
target = 5
nums = [1,3,5,6]
target = 2
# nums=[1,3,5,6]
# target=7
# nums=[2,3,5,6,9]
# target=7
ans=searchInsert(nums, target)