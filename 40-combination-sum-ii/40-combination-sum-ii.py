from collections import deque
import copy
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        l_c = len(candidates)
        r_d = deque()
        pre_str = ''
        for idx, k in enumerate(candidates):
            t_l = [k]
            r_d.append([t_l, k, idx+1])
        while r_d:
            t = r_d.popleft()
            s_idx = t[2]
            c_str = ''.join(str(e) for e in t[0])
            if c_str == pre_str:
                pre_str = c_str
                continue
            pre_str = c_str
            if (target - t[1]) > 0:
                for c_idx in range(s_idx, l_c):
                    t_d = copy.deepcopy(t[0])
                    c = candidates[c_idx]
                    t_d.append(c)
                    r_d.append([t_d, t[1]+c, c_idx+1])
            elif (target - t[1]) == 0:
                result.append(t[0])
        return result