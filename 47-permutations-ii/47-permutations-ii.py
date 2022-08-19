from collections import deque
import copy
def rP(r, r_list, str_list, n, l_n, nums, v):
    if n == l_n:
        s_r = ''.join([str(e) for e in list(r)])
        if not s_r in str_list:
            r_list.append(list(r))
            str_list.append(s_r)
        return r_list, str_list
    for idx, i_n in enumerate(nums):
        if v[idx] == False:
            v[idx] = True
            r.append(i_n)
            r_list, str_list = rP(copy.deepcopy(r), r_list, str_list, n+1, l_n, nums, v)
            r.pop()
            v[idx] = False
    return r_list, str_list
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result, str_list = rP(deque(), [], [], 0, len(nums), nums, [False for _ in range(len(nums))])
        return result