class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c_n = nums[0]
        c_i = 0
        t_l = []
        for idx, n in enumerate(nums):
            if c_n == n:
                if c_i < 2:
                    t_l.append(c_n)
                    c_i += 1
            else:
                c_n = n
                c_i = 0
                t_l.append(c_n)
                c_i += 1
                
        for idx, t in enumerate(t_l):
            nums[idx] = t
        
        for idx in range(len(t_l), len(nums)):    
            nums[idx] = '_'
        return len(t_l)