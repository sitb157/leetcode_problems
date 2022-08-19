from collections import deque
import copy
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        l_c = len(candidates)
        r_d = deque()
        for idx, k in enumerate(candidates):
            t_l = [k]
            r_d.append([t_l, k, idx])
        while r_d:
            t = r_d.popleft()
            s_idx = t[2]
            if (target - t[1]) > 0:
                for c_idx in range(s_idx, l_c):
                    t_d = copy.deepcopy(t[0])
                    c = candidates[c_idx]
                    t_d.append(c)
                    r_d.append([t_d, t[1]+c, c_idx])
            elif (target - t[1]) == 0:
                result.append(t[0])
        return result