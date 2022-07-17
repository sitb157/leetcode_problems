class Solution:
    def longestPalindrome(self, s: str) -> str:
        j = 0
        l = 0
        for i in range(len(s)):
            if s[i-l:i+1] == s[i-l:i+1][::-1]:
                j = i-l
                l = l+1
            if i-l > 0 and s[i-l-1:i+1] == s[i-l-1:i+1][::-1]:
                j = i-l-1
                l = l+2
        return s[j:j+l]
