def sEIdx(target, nums, _idx, l_nums):
    _s_idx = _idx
    _e_idx = _idx
    while (_s_idx-1 > -1) and (nums[_s_idx-1] == target):
        _s_idx -= 1
    while (_e_idx+1 < l_nums) and (nums[_e_idx+1] == target):
        _e_idx += 1      
    return [_s_idx, _e_idx]
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l_nums = len(nums)
        s_idx = 0
        e_idx = l_nums - 1
        if l_nums == 0:
            return [-1, -1]
        m_idx = int(l_nums/2)
        if nums[s_idx] == target:
            return sEIdx(target, nums, s_idx, l_nums)
        if nums[e_idx] == target:
            return sEIdx(target, nums, e_idx, l_nums)
        if nums[m_idx] == target:
            return sEIdx(target, nums, m_idx, l_nums)
        
        while ((e_idx - s_idx) > 1):
            m_idx = int((s_idx+e_idx)/2)
            print(m_idx)
            if target == nums[m_idx]:
                return sEIdx(target, nums, m_idx, l_nums)
            if (nums[s_idx] < target) and (target < nums[m_idx]):
                s_idx = s_idx
                e_idx = m_idx
            elif (nums[m_idx] < target) and (target < nums[e_idx]):
                s_idx = m_idx
                e_idx = e_idx
            else:
                return [-1, -1]
        return [-1, -1]