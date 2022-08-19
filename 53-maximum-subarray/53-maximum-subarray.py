class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def rDc(idx, nums, results):
            if (idx == (len(nums) - 1)):
                results[idx] = nums[idx]
            else:
                results[idx] = max(rDc(idx+1, nums, results)[idx+1]+nums[idx], nums[idx])
            return results
        
        results = [0 for _ in range(len(nums))]
        return max(rDc(0, nums, results))
        