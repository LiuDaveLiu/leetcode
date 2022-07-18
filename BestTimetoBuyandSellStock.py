def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """   
    pt_2=1
    pt_1=0
    ans=0    
    while pt_2<len(prices):
        if prices[pt_2]>prices[pt_1]:
            ans=max(prices[pt_2]-prices[pt_1],ans)
        else:
            pt_1=pt_2
        pt_2+=1
    return ans
        
prices = [7,1,5,3,6,4]
# prices = [7,6,4,3,1]
# prices = [2,4,1]
a=maxProfit(prices)