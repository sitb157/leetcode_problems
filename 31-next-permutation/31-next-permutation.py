class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        l_nums = len(nums)
        for i in range(l_nums-2, -1, -1):
            i_n = nums[i]
            m_n = max(nums) + 1
            print(i_n)
            print('****')
            j_idx = l_nums
            for j in range(l_nums-1, i, -1):
                j_n = nums[j]
                print(j_n)
                if i_n < j_n:
                    if m_n > j_n:
                        m_n = j_n
                        j_idx = j
                        
            if j_idx != l_nums:
                nums[i], nums[j_idx] = nums[j_idx], nums[i]
                print(nums)
                t_l = nums[i+1:]
                t_l.sort()
                for t, t_n in enumerate(t_l):
                    nums[i+1+t] = t_n
                return None
        return nums.sort()
        """
        Do not return anything, modify nums in-place instead.
        """
        