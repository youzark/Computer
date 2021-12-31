#! /usr/bin/env python
def editDistance(s ,t):
    cache = {}
    def recurse(m, n):
        """
        minimum distance between 
        fisrt letter from m in s
        first letter from n in t

        """
        if (m,n) in cache:
            return cache[(m,n)]
        if m == 0:
            result = n
        elif n == 0:
            result = m
        elif s[m - 1] == t[n - 1]:
            result = recurse(m-1 ,n-1)
        else:
            subcost = 1 + recurse(m-1 ,n-1)
            insertcost = 1 + recurse(m ,n-1)
            delcost = 1 + recurse(m-1 ,n)
            result = min(subcost,insertcost,delcost)
        cache[(m,n)] = result
        return result
    return recurse(len(s) ,len(t))

print(editDistance("a cat!" * 100,"the cats!" * 100))
