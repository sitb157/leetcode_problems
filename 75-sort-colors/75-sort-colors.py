class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r_s = ''
        w_s = ''
        b_s = ''
        for c in nums:
            if c == 0:
                r_s += '0'
            elif c == 1:
                w_s += '1'
            else:
                b_s += '2'
        t_s = r_s + w_s + b_s
        for idx, t in enumerate(list(t_s)):
            nums[idx] = int(t)
        