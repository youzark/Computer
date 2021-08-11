def computeDistance(s ,t):
    cache = {}
    def recurse(m ,n ):
        # return min distance between
        # first m's letters of s 
        # first n's letters of t
        if (m,n) in cache:
            return cache[(m,n)]
        if m == 0:
            result = n
        elif n == 0:
            result = m
        elif s[m - 1] == t[n - 1]:
            result = recurse(m - 1,n - 1)
        else:
            subCost = 1 + recurse(m - 1,n - 1)
            delCost = 1 + recurse(m - 1,n)
            insCost = 1 + recurse(m ,n - 1)
            result = min(subCost,delCost,insCost)
        cache[(m,n)] = result
        return  result
            
    return recurse(len(s),len(t))

    
print(computeDistance("a cat","the cats"))
print(computeDistance("a cat" * 10,"the cats" * 10))

