class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l_nums = len(nums)
        s_n = nums[0]
        s_idx = 0
        e_n = nums[-1]
        e_idx = l_nums - 1
        if s_n == target:
            return 0
        if e_n == target:
            return l_nums-1
        c_idx = int(l_nums/2)
        print(c_idx)
        m_n = nums[c_idx]
        if m_n == target:
            return c_idx
        if m_n < e_n:
            while (m_n < e_n) and (c_idx > 0):
                c_idx -= 1
                m_n = nums[c_idx]
            if (c_idx < 0):
                c_idx = int(l_nums/2)
            else:
                c_idx += 1
                
        elif m_n > e_n:
            while(m_n > e_n) and (c_idx < l_nums):
                c_idx += 1
                m_n = nums[c_idx]
        print(c_idx)
        
        if nums[c_idx] == target:
            return c_idx
        
        if (nums[s_idx] < target) and (target <= nums[c_idx-1]):
            c_j = c_idx - 1
            if target == nums[c_j]:
                return c_j
            while((c_j-s_idx) > 1):
                m_j = int((s_idx + c_j) / 2)
                if target == nums[m_j]: 
                    return m_j
                if (nums[s_idx] < target) and (target < nums[m_j]):
                    s_idx = s_idx
                    c_j = m_j
                elif (nums[m_j] <= target) and (target < nums[c_j]):
                    s_idx = m_j
                    c_j = c_j
                else:
                    return -1
                
        elif (nums[c_idx] < target) and (target < nums[e_idx]):
            c_j = c_idx
            while((e_idx-c_j) > 1):
                m_j = int((c_j + e_idx) / 2)
                if target == nums[m_j]: 
                    return m_j
                if (nums[c_j] < target) and (target < nums[m_j]):
                    c_j = c_j
                    e_idx = m_j
                elif (nums[m_j] <= target) and (target < nums[e_idx]):
                    c_j = m_j
                    e_idx = e_idx
                else:
                    return -1
        return -1
        print(c_idx)