from collections import deque
import copy
def rP(r, r_list, n, l_n, nums, v):
    if n == l_n:
        r_list.append(list(r))
        return r_list
    for idx, i_n in enumerate(nums):
        if v[idx] == False:
            v[idx] = True
            r.append(i_n)
            r_list = rP(copy.deepcopy(r), r_list, n+1, l_n, nums, v)
            r.pop()
            v[idx] = False
    return r_list
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return rP(deque(), [], 0, len(nums), nums, [False for _ in range(len(nums))])