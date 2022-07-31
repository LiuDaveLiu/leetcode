def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    hashmap={}
    ans=[]
    for i in nums1:
        if i in hashmap:
            hashmap[i]+=1
        else:
            hashmap[i]=1
    for i in nums2:
        if i in hashmap and hashmap[i]>0:
            ans.append(i)
            hashmap[i]-=1
    return ans
            
nums1 = [1,2,2,1]
nums2 = [2,2]
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
ans=intersect(nums1,nums2)