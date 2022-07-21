class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        nums.sort()
        print(nums)
        l_nums = len(nums)
        for i, i_n in enumerate( nums[:l_nums - 3]):
            #print(i)
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,l_nums-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                left = j + 1
                right = l_nums - 1
                #print(i, j)
                while(left < right):
                    total = i_n + nums[j] + nums[left] + nums[right]
                    gap = total - target
                    #print(i, j, left, right, total)
                    if gap > 0:
                        right -= 1
                    elif gap < 0:
                        left += 1
                    else:
                        results.append([i_n, nums[j], nums[left], nums[right]])
                        while (left < right) and (nums[left] == nums[left+1]):
                            left += 1
                        while (left < right) and (nums[right] == nums[right-1]):
                            right -= 1
                        left += 1
                        right -= 1
        return results