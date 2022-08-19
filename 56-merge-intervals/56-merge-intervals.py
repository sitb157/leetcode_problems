from collections import deque
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        d = deque()
        d.append(intervals[0])
        for i_t in intervals[1:]:
            t = d.pop()
            print(t)
            if t[1] >= i_t[0]:
                d.append([min(t[0], i_t[0]), max(t[1], i_t[1])])
            else:
                d.append(t)
                d.append(i_t)
        return list(d)