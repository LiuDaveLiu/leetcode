def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    
    #return str(x)==str(x)[::-1]
    if x<0 or (x%10==0 and x!=0):
        return False
    rev_x=0
    while x>rev_x:
        rev_x=rev_x*10+x%10
        x= x//10
      
    return rev_x==x or rev_x//10==x 

x=1221
ans=isPalindrome(x)