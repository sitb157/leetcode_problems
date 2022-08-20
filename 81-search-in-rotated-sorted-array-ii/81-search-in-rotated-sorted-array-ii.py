class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        c_idx = 0
        n_l = len(nums)
        l = n_l-1
        s = 0
        s_n = nums[s]
        l_n = nums[l]
        min_n = s_n
        max_n = l_n
        max_i = n_l - 1
        min_i = 0
        s_c = True
        for idx in range(n_l-1):
            if nums[idx] > nums[idx+1]:
                c_idx = idx
                max_n = nums[c_idx]
                min_n = nums[c_idx+1]
                s_c = False
                break
                
        if s_n == target or l_n == target or min_n == target or max_n == target:
            return True
        
        if not s_c:
            if (s_n < target < max_n):
                s = 0
                l = c_idx
            if (min_n < target < l_n):
                s = c_idx + 1
                l = n_l - 1
            
        while ((l-s) > 1):
            c_idx = s + int((l - s) / 2)
            if nums[c_idx] == target:
                return True
            if nums[s] < target < nums[c_idx]:
                s = s
                l = c_idx
            elif nums[c_idx] < target < nums[l]:
                s = c_idx
                l = l
            else:
                return False
        return False
        