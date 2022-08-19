from collections import deque
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l_n = len(nums)
        if l_n == 1:
            return True
        d = deque()
        d.append([0, nums[0]])
        while d:
            t = d.popleft()
            c_idx = t[0]
            c_n = t[1]
            m_n = 0
            m_idx = 0
            if (c_idx + c_n) >= (l_n - 1):
                return True
            for idx, n in enumerate(nums[c_idx+1:c_idx+c_n+1]):
                if m_n < (n + idx):
                    m_n = (n + idx) 
                    m_idx = c_idx + idx + 1
            if not m_n == 0:
                d.append([m_idx, nums[m_idx]])
        return False
                    