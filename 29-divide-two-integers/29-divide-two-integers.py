class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        return min(max(int(dividend / divisor), (-2**31)), (2**31-1))
        