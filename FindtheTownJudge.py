def findJudge(n, trust):
    """
    :type n: int
    :type trust: List[List[int]]
    :rtype: int
    """
    dest=dict()
    sour=dict()
    for i in range(1, n+1):
        dest[i]=0
        sour[i]=0
        
    for i in trust:
        dest[i[1]]=dest[i[1]]+1
        sour[i[0]]=sour[i[0]]+1

    people=list(dest.values())

    people=[x for x in people if x != []]
    mode=max(people)
    judge=people.index(mode)+1
    if mode==n-1 and sour[judge]==0:
        return judge
    else: return -1

             
    

n = 3
trust = [[1,3],[2,3]]
# n = 3
# trust = [[1,3],[2,3],[3,1]]
# n=3
# trust=[[1,2],[2,3]]
# n=4
# trust=[[1,3],[1,4],[2,3],[2,4],[4,3]]
ans=findJudge(n, trust)


    