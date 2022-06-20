def removeDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i = 0
    while i < len(nums):
        if nums[i] in nums[:i]:
            nums.remove(nums[i])
            i-=1
        else:
            i+=1
    return len(nums)

# nums=[1,1,2]
#nums = [0,0,1,1,1,2,2,3,3,4]