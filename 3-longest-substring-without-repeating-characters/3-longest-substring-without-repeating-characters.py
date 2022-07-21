class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_s = []
        max_num = 0
        for s_ in s:
            if s_ in max_s:
                if max_num < len(max_s):
                    max_num = len(max_s)
                for idx in range(len(max_s)):
                    if s_ == max_s[idx]:
                        max_s.append(s_)
                        max_s = max_s[idx+1:]
                        break
            else:
                max_s.append(s_)
        if max_num < len(max_s):
            max_num = len(max_s)
        return max_num