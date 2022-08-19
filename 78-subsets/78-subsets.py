from collections import deque
def rC(nums, k, result, s, q):
    if len(q) == k:
        result.append(list(q))
        return result
    for i in range(s, len(nums)):
        q.append(nums[i])
        result = rC(nums, k, result, i+1, q)
        q.pop()
    return result

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = list()
        for k in range(len(nums)+1):
            for r in rC(nums, k, list(), 0, deque()):
                results.append(r)
        return results