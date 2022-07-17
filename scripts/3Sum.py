class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        #print(nums)
        l_num = len(nums)
        result = []
        for i in range(l_num - 2):
            if (i > 0) and (nums[i] == nums[i-1]):
                continue
            l, r = i + 1, l_num - 1
            
            while l < r:
                t = nums[i] + nums[l] + nums[r]
                if t > 0:
                    r -= 1
                elif t < 0:
                    l += 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    while (l < r) and nums[l] == nums[l+1]:
                        l += 1
                    while (l < r) and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return result
