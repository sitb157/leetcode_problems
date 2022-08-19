from collections import deque
def rC( n, k, result, s, q):
    if len(q) == k:
        result.append(list(q))
        return result
    for i in range(s+1, n+1):
        q.append(i)
        result = rC(n, k, result, i, q)
        q.pop()
    return result

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:    
        return rC(n, k, list(), 0, deque())