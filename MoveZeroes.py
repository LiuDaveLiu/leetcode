def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    pt1=pt2=0
    while pt1<len(nums):
        if nums[pt1]!=0:
            nums[pt2],nums[pt1]=nums[pt1],nums[pt2]         
            pt1=pt2
            pt2+=1           
        pt1+=1
            
nums=[0, 0,1]
# nums=[0]
# nums = [0,1,0,3,12]
moveZeroes(nums)