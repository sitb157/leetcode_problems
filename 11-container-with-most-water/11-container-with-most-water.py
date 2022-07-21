class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        left = 0
        right = len(height)-1
        while(left < right):
            w = (right - left) * min(height[left], height[right])
            result = max(result, w)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return result