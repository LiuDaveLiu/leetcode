def titleToNumber(columnTitle):
    """
    :type columnTitle: str
    :rtype: int
    """
    hashmap={'A': 1, 'B': 2, 'Y': 25, 'Z': 26}
    ans=0
    for i in range(len(columnTitle)):
        ans+=hashmap[columnTitle[i]]*26**(len(columnTitle)-i-1)
    return ans

columnTitle = "A"
columnTitle = "AB"
columnTitle = "ZY"
ans=titleToNumber(columnTitle)