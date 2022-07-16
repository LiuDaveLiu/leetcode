def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """

    while m>0 and n>0:               
        if nums1[m-1]<=nums2[n-1]:
            nums1[n+m-1]=nums2[n-1]
            n-=1
        elif nums1[m-1]>nums2[n-1]:
            nums1[n+m-1]=nums1[m-1]
            m-=1

    while n>0:
        nums1[n-1]=nums2[n-1]
        n-=1
        
    # if nums1[pt1]<=nums2[pt2] and pt1>m-1:
    #     nums1[pt1+n-pt2]=nums2[pt2]
    #     pt2+=1
        
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
a=merge(nums1, m, nums2, n)

# nums1 = [4,0,0,0,0,0]
# m =1
# nums2 = [1,2,3,5,6]
# n=5
# a=merge(nums1, m, nums2, n)