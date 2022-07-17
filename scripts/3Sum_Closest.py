class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        max_gap = float('inf')
        closest_num = 0
        l_nums = len(nums)
        nums.sort()
        for i, i_n in enumerate(nums[:l_nums - 2]):
            #if i > 0 and nums[i] == nums[i-1]:
            #    continue
            left = i + 1
            right = l_nums - 1
            while (left < right):
                total = i_n + nums[left] + nums[right]
                gap = total - target 
                if gap > 0:
                    right -= 1
                elif gap < 0:
                    left += 1
                else:
                    return target
                if abs(gap) < max_gap:
                    max_gap = abs(gap)
                    closest_num = total 
                #while (left < right) and nums[left] == nums[left + 1]:
                #    left += 1
                #while (left < right) and nums[right] == nums[right - 1]:
                #    right -= 1
        return closest_num
