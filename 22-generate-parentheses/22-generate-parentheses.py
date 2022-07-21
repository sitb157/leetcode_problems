def rG(s, l, r, n, results):
    if (l == n) and (r == n):
        return results.append(s)
    if l < n:
        rG(s+'(',l+1,r, n, results)
    if l > r:
        rG(s+')',l,r+1, n, results)
    
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        rG('', 0, 0, n, results)
        return results