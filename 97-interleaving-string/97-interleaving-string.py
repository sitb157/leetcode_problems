from collections import deque
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1_l = list(s1)
        s2_l = list(s2)
        s3_l = list(s3)
        d = deque()
        d.append([0, 0])
        v = set((0, 0))
        c1 = False
        c2 = False
        if len(s1_l) == 0 and len(s2_l) == 0 and len(s3_l) == 0:
            return True
        if (len(s1_l) + len(s2_l)) != len(s3_l):
            return False
        
        while d:
            t = d.popleft()
            s1_idx = t[0]
            s2_idx = t[1]
            s3_idx = s1_idx + s2_idx
            if s3_idx == len(s3_l):
                #if not c1 * c2:
                #    if len(s1_l) == 0:
                #        if len(s2_l) > len(s3_l):
                #            return False
                #        return True
                #    if len(s2_l) == 0:
                #        if len(s1_l) > len(s3_l):
                #            return False
                #        return True
                #    return False
                return True
            if s1_idx < len(s1_l):
                if s1_l[s1_idx] == s3_l[s3_idx] and (s1_idx+1, s2_idx) not in v:
                    v.add((s1_idx+1, s2_idx))
                    d.append([s1_idx+1, s2_idx])
                    c1 = True
            if s2_idx < len(s2_l):
                if s2_l[s2_idx] == s3_l[s3_idx] and (s1_idx, s2_idx+1) not in v:
                    v.add((s1_idx, s2_idx+1))
                    d.append([s1_idx, s2_idx+1])
                    c2 = True
        return False
        