class Solution:
    def jump(self, nums: List[int]) -> int:
        iter_ = 0
        max_step = nums[0]
        l_n = len(nums)
        c_idx = 0 
        while (c_idx < (l_n-1)):
            temp_s = 0
            temp_idx = 0
            for idx, i_n in enumerate(nums[c_idx+1:c_idx+max_step+1]):
                if (c_idx+idx+1== l_n - 1):
                    return iter_ + 1
                if temp_s <= (i_n + idx):
                    temp_s = i_n + idx
                    temp_idx = idx
                    
            max_step = temp_s - temp_idx
            c_idx = c_idx + temp_idx + 1
            iter_ += 1
            print(c_idx, max_step)

            if (c_idx == (l_n -1)):
                return iter_

            if ((c_idx + max_step) >= (l_n - 1)):
                return iter_ + 1
            
        return iter_
