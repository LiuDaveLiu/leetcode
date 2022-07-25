def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    set_s=set(s+t)
    for i in set_s:
        if s.count(i)!=t.count(i): return False
    return True

s = "anagram"
t = "nagaram"
ans=isAnagram(s, t)